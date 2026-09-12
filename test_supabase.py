from supabase import create_client

SUPABASE_URL = "https://sjsuqwikjoiycvgrdgah.supabase.co"
SUPABASE_KEY = "sb_publishable_hC0bOoPMPlPtAWjTsb1-hQ__V4oinaz"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

try:
    response = supabase.table("alerts").insert({
        "message": "Test alert from Apki Suraksha",
        "image_url": "test.jpg"
    }).execute()

    print("SUCCESS: SUPABASE CONNECTED")
    print(response.data)

except Exception as e:
    print("SUPABASE ERROR:")
    print(e)