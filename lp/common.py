
class ReportResult:
    def __init__(self):
        self.vf_src = None
        self.vf_result = None
        self.max_of_max = None
        self.avg_of_max = None
        self.avg_of_p99 = None
        self.avg_of_stddev = None
        self.avg_of_rps = None

    def __str__(self):
        s = f"max(max)={self.max_of_max}\n"+\
            f"avg(max)={self.avg_of_max}\n"+\
            f"avg(p99)={self.avg_of_p99}\n"+\
            f"avg(rps)={self.avg_of_rps}\n"+\
            f"avg(stddev)={self.avg_of_stddev}"

        return s

    def __repr__(self):
        return str(self)
