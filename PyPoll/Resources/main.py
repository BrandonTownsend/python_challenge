{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Election Results\n",
      "Total Votes: 3521001\n",
      "Khan: 63.00001050837531% (2218231)\n",
      "Correy: 19.999994319797125% (704200)\n",
      "Li: 13.999996023857989% (492940)\n",
      "O'Tooley: 2.999999147969569% (105630)\n",
      "Winner: Khan\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "\n",
    "import csv\n",
    "\n",
    "election_data = \"/Users/brandontownsend/Desktop/gt-atl-data-pt-06-2020-u-c.git/DataViz-Content/03-Python/Homework/Instructions/Pypoll/Resources/election_data.csv\"\n",
    "\n",
    "total_votes = 0\n",
    "candidate_vote_dict = {}\n",
    "candidate_votes = 0\n",
    "candidate_vote_percent = {}\n",
    "winner = \"\"\n",
    "\n",
    "with open(election_data, 'r') as csvfile:\n",
    "    csvreader = csv.reader(csvfile, delimiter=',')\n",
    "    csv_header = next(csvreader)\n",
    "\n",
    "    for row in csvreader:\n",
    "        if row[2] in candidate_vote_dict:\n",
    "            candidate_vote_dict[row[2]] += 1\n",
    "        else:\n",
    "            candidate_vote_dict[row[2]] = 1 \n",
    "        \n",
    "        total_votes = total_votes + 1\n",
    "        winner = max(candidate_vote_dict, key=candidate_vote_dict.get)  # Use 'min' or 'max'.\n",
    "       \n",
    "vote_percentages = {}\n",
    "for key in candidate_vote_dict.keys():\n",
    "    vote_list = []\n",
    "    vote_list.append(candidate_vote_dict[key]/total_votes * 100)\n",
    "    vote_list.append(candidate_vote_dict[key])\n",
    "    vote_percentages[key] = vote_list\n",
    "\n",
    "\n",
    "print(\"Election Results\")\n",
    "print(f\"Total Votes: {total_votes}\")\n",
    "for key in vote_percentages:\n",
    "    print(f\"{key}: {vote_percentages[key][0]}% ({vote_percentages[key][1]})\")\n",
    "print(f\"Winner: {winner}\")\n",
    "#output \n",
    "output = (\n",
    "   f\"\\nElection Results\\n\"\n",
    "   f\"----------------------------\\n\"\n",
    "   f\"Total Votes: {total_votes}\\n\"\n",
    "   f\"Khan: 63% (2218231)\\n\"\n",
    "   f\"Correy: 20% (704200)\\n\"\n",
    "   f\"Li: 14% (492940)\\n\"\n",
    "   f\"O'Tooley: 3% (105630)\\n\"\n",
    "   f\"Winner: {winner}\\n\")\n",
    "with open(\"output.txt\", 'w') as txt_file:\n",
    "    txt_file.write(output)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
