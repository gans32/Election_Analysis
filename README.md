# Election Analysis

## Overview

The purpose of this challenge is to determine the results of a local election. The specific data gathered is the total number of votes cast, voter turnout of each county involved, county with the largest voter turnout, number and percentage of votes for each candidate, and the winning candidate's information. All of the election data is stored in [this csv file.](resources/election_results.csv) 

## Results

The program's report on the election results can be found in [this text file in the repository.](analysis/election_analysis.txt)

* The total number of votes cast was 369,711. We got this number by initializing a total vote counter that incremented by one each time the program iterated through the csv file's rows.

* Votes from three counties were included in the count: Jefferson, Denver, and Arapahoe. These are the results.
  - Jefferson: 10% (38855)
  - Denver: 82% (306055)
  - Arapahoe: 6% (24801)
We got the voter turnout for each county, as well as the percentage of the total votes that came from each county, using this code:
```
    for county in county_list:
        total_county_vote = county_votes[county]

        total_county_percent = float(total_county_vote) / float(total_votes) * 100

        county_results = (
            f"{county}: {int(total_county_percent)}% ({total_county_vote})\n"
        )
```

* The county with the largest voter turnout was Denver, with 306,055 votes.

* Votes for three candidates were included in the count: Charles Casper Stockham, Diana Degette, and Raymon Anthony Doane. These are the results:
  - Charles Casper Stockham: 23.0% (85,213)
  - Diana DeGette: 73.8% (272,892)
  - Raymon Anthony Doane: 3.1% (11,606)

We got these results for the candidates using this code:
```
for candidate_name in candidate_votes:

        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
```

* Based on this data, the winning candidate is Diana Degette, with 73.8% of the vote and a total of 272,982 votes.

## Summary

With simple modifications, this script can be run to get the results of other elections too. The values of candidate_name and county_name are defined by specific row indices in the dataset, so with a different dataset the definition of those variables would need to be modified. Setting these values according to the value of a column header rather than a row index could make the script more standardizable to other datasets; otherwise, the specific indices definining those variables would need to match the present dataset. The script can easily apply to datasets with different numbers of counties and candidates and will still produce an accurate result. 
