
#for computing scores
def compute_scores(pet_report_block, selected_time):
    location_counts = pet_report_block.get(selected_time,{})
    
    # taketotal reports given time-range 
    total_reports = sum(location_counts.values())

    location_probabilities = {}
    if total_reports > 0:
        #For each location, compute the likelihood score and convert to precent
        for loc, count in location_counts.items():
            score_percentage = round((count / total_reports) * 100)
            
            # store in dictionary so loc: percentage 
            location_probabilities[loc] = score_percentage
    return location_probabilities


#sorting the score start from highest likelihood 
def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index][1] >= right[right_index][1]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result


# main func
def get_ranked_results(pet_info, time_range):
    #  checks if the sent pet has values thus is not empty or doesn't exist in db
    if not pet_info: return []  
    # check if time-range exists for that pet.
    if time_range not in pet_info: return []
        
    #compute score
    scores = compute_scores(pet_info, time_range)
    
    #turn to list
    scores_list = list(scores.items())
    
    # call mergesort to rank by desc order
    sorted_results = merge_sort(scores_list)
    return sorted_results