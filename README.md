After carefully examining the events calculations function and the wood Mc signal in Kmsweb, I have made some improvements to enhance productivity. Here are the revised instructions:

1. Upon analyzing the data, specifically the wood_mc cleaned values from the wu_end_idx:
   
   a. For batch number 1788 (k-23-03) as an example, it is observed that wood_mc cleaned never falls below 30%. In such cases, we need to modify the code to set the Phase2 start index as the end of the warm-up phase, indicating the absence of Phase 1.

   b. For batch number 1952 (k-23-03), it is noticed that wood_mc cleaned is always below 30% and never reaches 30%. In this scenario, neither phase1 nor phase2 will be detected.

2. To handle both of the aforementioned cases, the code should be adjusted as follows:

   a. Extract the wood mc signal from the warm-up phase's end index to the Phase2 index. Then, calculate the maximum value of this signal. If the maximum value is below 30% (indicating that wood mc never reached 30%), set idx_phase2_start as idx_phase2_end. The same logic applies to Phase 1 detection (in cases where both phases are absent).

   b. Conversely, if the minimum value of the extracted signal is greater than 30%, it implies that wood mc always remains above 30% and never falls below it. In this situation, Phase2 should start at the wu_end_idx index, while Phase1 detection is not required.

3. Additionally, if wood_mc falls below 30% multiple times, Phase2 should commence from the index of the last wood_mc fall.

By implementing these improved instructions, we can make the process more productive and efficient in handling various scenarios related to wood_mc values and phase detection.
