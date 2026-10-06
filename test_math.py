from vscas.similarity import (
    dot_product,
    euclidean_norm,
    cosine_similarity
)


# Test vectors
A = [1, 2, 3]
B = [4, 5, 6]


print("================================")
print("   VSCAS MATHEMATICAL ENGINE")
print("================================")

print("\nVector A:", A)
print("Vector B:", B)

print("\nDot Product:")
print(dot_product(A, B))

print("\nEuclidean Norm:")
print("||A|| =", euclidean_norm(A))
print("||B|| =", euclidean_norm(B))

print("\nCosine Similarity:")
print(cosine_similarity(A, B))

print("\n================================")