import asyncio
from django.http import JsonResponse

async def async_view(request):
    async def count():
        for i in range(1, 11):
            await asyncio.sleep(1)  #Aguarda 1 segundo para chamar o proximo numero
            print(i) 
        return 'Contagem concluída'

    loop = asyncio.get_event_loop()
    result = await loop.create_task(count())
    return JsonResponse({'result': result})
