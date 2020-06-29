{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Financial Analysis\n",
      "Total Months: 86\n",
      "Total: $74638024\n",
      "Average Change: $-2315.1176470588234\n",
      "Greatest Increase in Profits: Feb-2012 ($1926159)\n",
      "Greatest Decrease in Profits: Sep-2013 ($-2196167)\n"
     ]
    }
   ],
   "source": [
    "#Brandon Townsend\n",
    "\n",
    "import os\n",
    "import csv\n",
    "\n",
    "pybank_path = \"/Users/brandontownsend/gt-atl-data-pt-06-2020-u-c/DataViz-Content/03-Python/Homework/Instructions/PyBank/Resources/budget_data.csv\"\n",
    "\n",
    "total_month = 0\n",
    "month_of_change = []\n",
    "net_change_list = []\n",
    "greatest_increase = [\"\", 0]\n",
    "greatest_decrease = [\"\", 999999999999999]\n",
    "total_net = 0\n",
    "\n",
    "with open(pybank_path, newline='') as csvfile:\n",
    "    csvreader = csv.reader(csvfile, delimiter=',')\n",
    "\n",
    "\n",
    "    csv_header = next(csvreader)\n",
    "\n",
    "    first_row = next(csvreader)\n",
    "    total_month = total_month + 1\n",
    "    total_net = total_net + int(first_row[1])\n",
    "    previous_net = int(first_row[1])\n",
    "\n",
    "    \n",
    "    for row in csvreader:\n",
    "        total_month = total_month + 1\n",
    "        total_net = total_net + int(first_row[1])\n",
    "        net_change = int(row[1]) - previous_net\n",
    "        previous_net = int(row[1])\n",
    "        net_change_list = net_change_list + [net_change]\n",
    "        month_of_change = month_of_change + [row[0]]\n",
    "        if net_change > greatest_increase[1]:\n",
    "            greatest_increase[0] = row[0]\n",
    "            greatest_increase[1] = net_change\n",
    "        if net_change < greatest_decrease[1]:\n",
    "            greatest_decrease[0] = row[0]\n",
    "            greatest_decrease[1] = net_change\n",
    "\n",
    "net_monthly_average = sum(net_change_list)/len(net_change_list)\n",
    "print(\"Financial Analysis\")\n",
    "print(f\"Total Months: {total_month}\")\n",
    "print(f\"Total: ${total_net}\")\n",
    "print(f\"Average Change: ${net_monthly_average}\")\n",
    "print(f\"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\")\n",
    "print(f\"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\")\n",
    "\n",
    "\n",
    "output = (\n",
    "   f\"\\nFinancial Analysis\\n\"\n",
    "   f\"----------------------------\\n\"\n",
    "   f\"Total Months: {total_month}\\n\"\n",
    "   f\"Total: ${total_net}\\n\"\n",
    "   f\"Average  Change: ${net_monthly_average}\\n\"\n",
    "   f\"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\\n\"\n",
    "   f\"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\\n\")\n",
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
