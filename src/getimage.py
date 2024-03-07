from asyncio import run

from httpx import AsyncClient

from src.config import SIMEPAR_IMAGE_PATH_1, TIMEOUT, URL_SIMEPAR_IMAGE_RADAR_1


def sync_decompress_and_save_image(compressed_data: bytes) -> None:
	"""WARNING: This function is blocking, it should be used with caution."""
	with open(SIMEPAR_IMAGE_PATH_1, "wb") as f:
		f.write(compressed_data)


async def fetch_and_save_image() -> None:
	headers = {
		"authority": "lb01.simepar.br",
		"method": "GET",
		"path": "/riak/pgw-radar/product1.jpeg",
		"scheme": "https",
		"accept": (
			"image/avif,image/webp,image/apng,"
			"image/svg+xml,image/*,*/*;q=0.8"
		),
		"accept-encoding": "gzip, deflate, br",
		"accept-language": "en-US,en;q=0.9",
		"if-modified-since": "Thu, 07 Mar 2024 04:10:04 GMT",
		"if-none-match": '"5GW8QIgJUu3ajqCHffCSaj"',
		"referer": "http://www.simepar.br/",
		"sec-ch-ua": (
			'"Not A(Brand";v="99", ' '"Opera";v="107", "Chromium";v="121"'
		),
		"sec-ch-ua-mobile": "?0",
		"sec-ch-ua-platform": '"Linux"',
		"sec-fetch-dest": "image",
		"sec-fetch-mode": "no-cors",
		"sec-fetch-site": "cross-site",
		"user-agent": (
			"Mozilla/5.0 (X11; Linux x86_64) "
			"AppleWebKit/537.36 (KHTML, like Gecko) "
			"Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0"
		),
	}

	async with AsyncClient() as client:
		response = await client.get(
			URL_SIMEPAR_IMAGE_RADAR_1,
			headers=headers,
			timeout=TIMEOUT,
		)
		response.raise_for_status()
		sync_decompress_and_save_image(response.read())


async def main() -> None:
	await fetch_and_save_image()


if __name__ == "__main__":
	run(main())
