import cloudinary.uploader

async def upload_image(file):
    result = cloudinary.uploader.upload(
        file.file,
        folder = "vastre-category"
    )

    return {
        "url" : result["secure_url"],
        "public_id" : result["public_id"]
    }

async def destroy_image(category_public_id):
    cloudinary.uploader.destroy(category_public_id)

async def update_image(image,  category_public_id):
    result = cloudinary.uploader.upload(
        image.file,
        public_id = category_public_id,
        overwrite= True,
        invalidate = True
    )
    return {
        "url" : result["secure_url"]
    }