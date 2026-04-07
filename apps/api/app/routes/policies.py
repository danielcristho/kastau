from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query, Path
from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.policy import Policy
from app.schemas.policy import PolicyRead

router = APIRouter(prefix="/api/v1/policies", tags=["Kebijakan"])


@router.get(
    "",
    response_model=dict,
    summary="Daftar Semua Kebijakan",
    description="Mengambil daftar kebijakan daerah (Perda, Perbup, SK Bupati) dengan dukungan filter kategori, tahun, status, dan pencarian teks.",
)
def list_policies(
    category: Optional[str] = Query(None, description="Slug kategori kebijakan (contoh: 'pendidikan')"),
    year: Optional[int] = Query(None, description="Tahun kebijakan diterbitkan (contoh: 2024)"),
    status: Optional[str] = Query(None, description="Status kebijakan: 'berlaku', 'direvisi', atau 'dicabut'"),
    type: Optional[str] = Query(None, description="Jenis kebijakan: 'Perda', 'Perbup', atau 'SK Bupati'"),
    q: Optional[str] = Query(None, description="Kata kunci pencarian (judul, nomor, atau isi)"),
    page: int = Query(1, ge=1, description="Nomor halaman untuk pagination"),
    limit: int = Query(20, ge=1, le=100, description="Jumlah data per halaman"),
    db: Session = Depends(get_db),
):
    query = db.query(Policy)

    if category:
        query = query.filter(Policy.category == category)
    if year:
        query = query.filter(Policy.year == year)
    if status:
        query = query.filter(Policy.status == status)
    if type:
        query = query.filter(Policy.type == type)
    if q:
        query = query.filter(
            or_(
                Policy.title.ilike(f"%{q}%"),
                Policy.summary.ilike(f"%{q}%"),
                Policy.detail.ilike(f"%{q}%"),
                Policy.number.ilike(f"%{q}%"),
            )
        )

    total = query.count()
    items = query.offset((page - 1) * limit).limit(limit).all()

    return {
        "total": total,
        "page": page,
        "limit": limit,
        "items": [PolicyRead.model_validate(item) for item in items],
    }


@router.get(
    "/{id}",
    response_model=PolicyRead,
    summary="Detail Kebijakan",
    description="Mengambil informasi lengkap tentang satu kebijakan berdasarkan ID-nya.",
)
def get_policy(id: int = Path(..., description="ID unik kebijakan"), db: Session = Depends(get_db)):
    policy = db.query(Policy).filter(Policy.id == id).first()
    if not policy:
        raise HTTPException(status_code=404, detail="Kebijakan tidak ditemukan")
    return policy
