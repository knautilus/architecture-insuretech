## Задание 5. Проектирование GraphQL API

Исходный Swagger контракт:

[Swagger](swagger.txt)

Итоговая GraphQL-схема:

[GraphQL](schema.graphql)

Пример запроса для получения клиента по Id вместе со списком его документов:

```
query
{
  client (id: "1")
  {
    id
    name
    age
    documents
    {
      id
      type
      number
      issueDate
      expiryDate
    }
  }
}
```