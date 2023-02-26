# Parsing JSON in potgres 
    ->
    ->>
    ::json
    json_array_elements()

# String slipt function
    split_part(column, delimiter, index)

```select distinct split_part(duration::TEXT, ' ', 2) as units  from (
select json_array_elements(response::json -> 'unit' -> 'items') ->> 'content_info_short'  as duration from app_scraprequestresponse as2
) as timeinstring;
```
