import os
import shutil
import zipfile
import subprocess

# 1. Hedef klasörü oluştur
os.makedirs("goturn_model", exist_ok=True)
os.chdir("goturn_model")

# 2. Git repo klonla (Mogball'un dosya deposu)
if not os.path.exists("goturn-files"):
    print("🔽 goturn-files reposu indiriliyor...")
    subprocess.run(["git", "clone", "--depth=1", "https://github.com/Mogball/goturn-files.git"])
else:
    print("✅ Repo zaten var, atlanıyor.")

# 3. Dosyaları kopyala
src_path = os.path.join("goturn-files")
print("📁 Dosyalar kopyalanıyor...")

# .zip parçaları ve prototxt dosyasını al
for file in os.listdir(src_path):
    if file.startswith("goturn.caffemodel.zip.") or file == "goturn.prototxt":
        full_src = os.path.join(src_path, file)
        if os.path.isfile(full_src):
            shutil.copy(full_src, "../../..")

# 4. Zip parçalarını birleştir
print("📦 Zip parçaları birleştiriliyor...")
with open("goturn.caffemodel.zip", "wb") as outfile:
    for i in range(1, 5):  # 001-004
        part_filename = f"goturn.caffemodel.zip.{i:03d}"
        if not os.path.exists(part_filename):
            raise FileNotFoundError(f"❌ Eksik dosya: {part_filename}")
        with open(part_filename, "rb") as infile:
            outfile.write(infile.read())

# 5. Zip'i aç
print("🗃️ Dosya çıkarılıyor...")
with zipfile.ZipFile("goturn.caffemodel.zip", 'r') as zip_ref:
    zip_ref.extractall()

# 6. Sonuç
print("🎉 Tamamlandı! Aşağıdaki dosyalar hazır:")
print("- goturn.prototxt")
print("- goturn.caffemodel")
