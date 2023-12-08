# LittleLemon
## Auth endpoint
POST - get token
```
/restaurant/api-token-auth/

JSON
{
	"username": "your username",
	"password": "your password"
}
```
## Booking endpoint
GET - list all bookings(need token)
```
/restaurant/booking/tables/
```
## MenuItem endpoint
GET - list all menu items
```
/restaurant/menu/
```
---
GET - query single menu item
```
/restaurant/menu/<int:pk>
```
---
POST - create new menu item
```
/restaurant/menu/

JSON:
{
	"title": "Cake",
	"price": "4.30"
}
```
---
PUT - update menu item
```
/restaurant/menu/<int:pk>

JSON:
{
	"title": "Cake",
	"price": "4.30"
}
```
---
DELETE - delete menu item
```
/restaurant/menu/<int:pk>
```
---