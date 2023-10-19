def can_place_cows(free_sections, C, min_distance):
    cows_placed = 1
    last_position = free_sections[0]
    for i in range(1, len(free_sections)):
        if free_sections[i] - last_position >= min_distance:
            cows_placed += 1
            last_position = free_sections[i]
            
            if cows_placed == C:
                return True
    
    return False

def get_max_width(C, free_sections):
    if C == 2:
        return max(free_sections) - min(free_sections)

    free_sections.sort()  
    result = 0
    left, right = 0, free_sections[-1] - free_sections[0] 

    while left <= right:
        mid = (left + right) // 2
        if can_place_cows(free_sections, C, mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result

if __name__ == '__main__':
    print(get_max_width(C=4, free_sections=[1, 2, 3, 4, 5, 10, 30, 40, 60, 90]))
