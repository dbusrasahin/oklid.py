# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 14:15:07 2024

@author: Excalıbur
"""

points = [(1, 2), (4, 6), (5, 1), (7, 8), (9, 3)]

# öklid uygulayarak mesafe bulan fonksiyon
def euclideanDistance(point1, point2):
    x1, y1 = point1  # İlk nokta koordinatları
    x2, y2 = point2  # İkinci nokta koordinatları
    kenar1 = [(x2 - x1) ** 2]
    kenar2 = [(y2 - y1) ** 2]
    distance = (kenar1+kenar2) ** 0.5
    return distance

#öklid mesafelerini bulma
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafenin bulunması
min_distance = min(distances)

#sonuçların ekrana yazılması
print(f"Tüm mesafeler: {distances}")
print(f"Minimum mesafe: {min_distance}")