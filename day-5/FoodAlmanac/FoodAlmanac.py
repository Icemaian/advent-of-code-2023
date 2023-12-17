class ConversionMap():
    def __init__(self, source_id: str = "", destination_id: str = "", mapRanges: list[list] = []):
        self.source_id = source_id
        self.destination_id = destination_id
        self.mapRanges = {}
        numOfRows = 1
        for row in mapRanges:
            self.mapRanges[numOfRows] = self.convertRangeToMap(row)
            numOfRows += 1

    def convertRangeToMap(self, input: list[int]) -> {}:
        destRange = input[0]
        sourceRange = input[1]
        rangeLen = input[2]
        return {'destRange' : destRange, 'sourceRange' : sourceRange, 'rangeLen' : rangeLen}

    def convertUsingMap(self, input: int) -> int:
        result = None
        if input == None:
            raise Exception("Input cannot be none")
        for key, ranges in self.mapRanges.items():
            if input >= ranges["sourceRange"] and input <= (ranges['sourceRange'] + ranges['rangeLen'] - 1):
                result = (ranges['destRange'] + input - ranges['sourceRange'])
                print(f'    {input}->{result}, using map {ranges}')
        return result if result else input
            
class Almanac():
    def __init__(self, input_path: str):
        self.seeds = []
        self.mappings = dict()
        with open(input_path, 'r') as f:
            source_id = ''
            dest_id = ''
            mapRanges = []
            for line in f:
                line = line.replace('\n', '')
                if 'seeds' in line:
                   self.seeds.extend(list(map(int, line.replace('seeds: ', '').split(' '))))
                elif line != "" and line[0].isnumeric():
                    mapRanges.append(list(map(int,line.split(' '))))
                elif 'map' in line:
                    line_formated = line.replace(' map:', '').split('-')
                    source_id = line_formated[0]
                    dest_id = line_formated[2]
                elif source_id and mapRanges and line == "":
                    self.mappings[source_id] = ConversionMap(source_id, dest_id, mapRanges) 
                    source_id = ''
                    dest_id = ''
                    mapRanges = []
            
            self.mappings[source_id] = ConversionMap(source_id, dest_id, mapRanges) 
            source_id = ''
            dest_id = ''
            mapRanges = []
    
    def mapValues(self, values: list[int] = [], startKey: str = 'seed', goalKey: str = 'location') -> list[int]:
        print(f'Starting with values:{values}, startKey:{startKey}, goalKey:{goalKey}')
        results = []
        mapper = ConversionMap()
        if not values:
            values = self.seeds
        for key, value in self.mappings.items():
            if key == startKey:
                mapper = value
                break
        for input in values:
            results.append(mapper.convertUsingMap(input))
        if mapper.destination_id != goalKey:
            results = self.mapValues(values=results,startKey=mapper.destination_id ,goalKey=goalKey)

        return results

    def findMin(self, input: list[int]) -> int:
        result = None
        for item in input:
            if result == None:
                result = item
            else:
                print(f'curr item: {item}, vs current min:{result}')
                if item < result:
                    result = item
        return result
