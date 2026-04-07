from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.category import Category
from app.models.policy import Policy
from app.schemas.category import CategoryRead, CategoryWithPolicies
from app.schemas.policy import PolicyRead

router = APIRouter(prefix="/api/v1/categories", tags=["Kategori"])


@router.get(
    "",
    response_model=list[CategoryRead],
    summary="Daftar Kategori Kebijakan",
    description="Mengambil semua kategori kebijakan yang tersedia (seperti Pendidikan, Kesehatan, dll) beserta jumlah peraturan di setiap kategori.",
)
def list_categories(db: Session = Depends(get_db)):
    categories = db.query(Category).all()
    result = []
    for cat in categories:
        count = (
            db.query(func.count(Policy.id))
            .filter(Policy.category == cat.slug)
            .scalar()
        )
        result.append(
            CategoryRead(
                slug=cat.slug,
                name=cat.name,
                description=cat.description,
                icon=cat.icon,
                policy_count=count,
            )
        )
    return result


@router.get(
    "/{slug}",
    response_model=CategoryWithPolicies,
    summary="Detail Kategori dan Kebijakan Terkait",
    description="Mengambil satu kategori spesifik beserta daftar kebijakan yang termasuk di dalamnya.",
)
def get_category(slug: str, db: Session = Depends(get_db)):
    cat = db.query(Category).filter(Category.slug == slug).first()
    if not cat:
        raise HTTPException(status_code=404, detail="Kategori tidak ditemukan")

    policies = db.query(Policy).filter(Policy.category == slug).all()

    return CategoryWithPolicies(
        slug=cat.slug,
        name=cat.name,
        description=cat.description,
        icon=cat.icon,
        policy_count=len(policies),
        policies=[PolicyRead.model_validate(p) for p in policies],
    )
