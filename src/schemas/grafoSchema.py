def grafoEntity(item) -> dict:
    return {
        'id': str(item['_id']),
        'name': item['name'],
        'descripcion': item['descripcion'],
        'nodes': item['nodes']
    }

def grafosEntity(items) -> list:
   return [grafoEntity(item) for item in items]