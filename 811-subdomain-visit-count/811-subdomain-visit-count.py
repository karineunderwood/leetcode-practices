class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = collections.defaultdict(int)
        
        for domain in cpdomains:
            count, domain = domain.split()
            
            count = int(count)
            
            frag = domain.split(".")
            
            for i in range(len(frag)):
                counts['.'.join(frag[i:])] += count
                
        return [f"{count} {domain}" for domain, count in counts.items()]
        
        