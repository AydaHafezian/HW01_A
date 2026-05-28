# استفاده از نسخه سبک پایتون
FROM python:3.11-slim

# تعیین پوشه کاری
WORKDIR /app

# کپی کردن پکیج‌های آفلاین
COPY pkg /app/pkg
COPY requirements.txt .

# ۱. نصب ابزارهای Build و وابستگی‌های اصلی (بدون نیاز به اینترنت)
RUN pip install --no-index --find-links=/app/pkg setuptools wheel typer click rich shellingham

# ۲. نصب پکیج‌های سنگین از میرور لیارا
RUN pip install pandas numpy --index-url https://package-mirror.liara.ir/repository/pypi/simple

# کپی کردن کل پروژه
COPY . .

# ۳. نصب پروژه به‌صورت Editable با حذف اجباری لایه Isolation
# استفاده از سوییچ مستقیم --no-build-isolation برای جلوگیری از مراجعه به pypi.org
RUN pip install --no-build-isolation -e . --no-deps

# دستور اجرا
CMD ["python", "-m", "airbnb_ops.cli"]





