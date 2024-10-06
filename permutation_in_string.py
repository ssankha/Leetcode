#567. Permutation in String
class Solution(object):
        
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        def check_to_remove(hashmap, key):
            if(hashmap[key] == 0):
                hashmap.pop(key)
                
        if(len(s1) > len(s2)):
            return False
                
        s1_table = {}
        window_table = {}
        for i in range(len(s1)):
            s1_char = s1[i]
            s2_char = s2[i]
            
            s1_table[s1_char] = s1_table.get(s1_char, 0) + 1
            window_table[s2_char] = window_table.get(s2_char, 0) + 1

        if(s1_table == window_table):
                return True
        
        #print(s1_table)
        #print()
        for i in range(len(s2) - len(s1)):
            #print(window_table)
            prev_char = s2[i]
            curr_char = s2[len(s1) + i]
            window_table[prev_char] -= 1
            check_to_remove(window_table, prev_char)
            window_table[curr_char] = window_table.get(curr_char, 0) + 1
            
            if(s1_table == window_table):
                return True
            
        return False
                

# test
sol = Solution()

s1 = "adc"
#s2 = "amwfpqwfwkarvhfcisywzaahtbdbuicxmjseeoudwfcdxetbmacayfikolbdxkocezhalfhxabwvuddcyazwiqiwefgolzvrpdxcuskpsmwhslpeygjrvvajajafppcwkqhxwkigemfullbqkvuqwfnqnhxiltyfcpfdyumfwyelmtzbdccmbvxedgfimmsqwxmopvxmuonuzyzlhpeunailpydcqybghdwvqxrpautsvrhfxprdqlgzownvincoxjnjwrqrdgpegtgvlifbbautkfqbhqiftbmxadvorqjnqlsceuctazxgofmchypspqvwyzoeejqfkvvwftvagajafmafvytslubpzalnahjknarjswkxmzzlmlokrifiopjcamvynmmuegnzvveetssuucqclbzxgjwbsflyelpdsvzicdnlenuxggcsrckfdixsqcjrzsbztgvxbpktlbdqrcqoatgxqhwehqiuqjnldursyzplwlcdvwrmlknviqtexwgqovwbcdugdblakufxcapvkvhraacetowtcypfxlvwmwdafesfgqezspbvqzxicblrdsmmdzunpcmzvysgbnspuldkppwlrsrnnewwjquhzrodmsbgbycvrzmtnskyuqqoqkxyakojewbbtntbdjuncpgbwgrtvewyscyujnqtpuaulrnjqmdujxydwzfyqfnxmjqogibxqeuqdxsdjjpootpzmhcvoeyvdspktyjzadkfwcdulsuktottgpvptjfydvpdxoznzhbkmitaiywqklwrktmzsyndnqmtapaaadzkynfxiwqxtekcbkmcwhwwdylvoxosxcexeceavpfptdlkyinhdobrnxfdbtuomjojmzeytlntkundrydqmkiayounnbhfxrlriuatzumgfcyniicwhtsaffhnxamwjtgbxvewtgovvrjvblrlvrghyoiicgvyorzjgecmxqeiwpuubfrnkmpynwywqczqdpeinebgfyrhouvifthoaariadurpbrexbfnuwgkbmgowjuaysnmidptzetckscxvxttdogpywxdvaktmkispgyghfazxyxslyjhqorndzpjepmwiuisfhvacnpkthbfrasndrfkfuhpetlnfugmqhqpvtvlwumhxduxxmugstcbksvqholothhftzungtxdysudnixkzekpdlgddnvyfuitcedxvjfsjxhbcrenufafxzdrumeavumdbvvgpodgtsjzznxkpbfltchmogigordwcpcanomjznfmsxpzqgxigjpybooxsgyiuxskowkdpypnzpgebowqefomcpmfilixgzvoffvmcypgyrwhwaelfpclzaoldlaimtnszckziyqewrtewpfyhphxruytifwtodznvxmxwoibqvtmynpqshnmiymrayaenoiknjqzwoltqhaganjdwzkncathqrgcigaguimqgznupmsikurxjltfydqiozmddxydgtsvwoloqtlqhryfqmcsfetvtjkauyjgillobotqfhzsyjtcjsiqxhwoaucluagbltdwroayydlwzytpqlsxkbrgcavvaqvlggewskeflsejklqexjvcudzaanxrgnkwygokcuxkvypsh"
s2 = "dcda"
result = sol.checkInclusion(s1, s2)
print(result)