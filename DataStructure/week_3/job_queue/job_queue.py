# python3

"""
Coursera Specialization: Data Structure and Algorithm
Course: Data Structure

week 3-2 Paralle processing

You have a program which is parallelized and uses 𝑛 independent threads to process the given list
of 𝑚 jobs. Threads take jobs in the order they are given in the input. If there is a free thread,
it immediately takes the next job from the list. If a thread has started processing a job, it doesn’t
interrupt or stop until it finishes processing the job. If several threads try to take jobs from the list
simultaneously, the thread with smaller index takes the job. For each job you know exactly how long
will it take any thread to process this job, and this time is the same for all the threads. You need to
determine for each job which thread will process it and when will it start processing.



"""
class Worker(object):
    def __init__(self, id):
      self.id = id
      self.next_free_time = 0

    def is_larger(self, other):
      if self.next_free_time == other.next_free_time:
        return self.id > other.id
      else:
        return self.next_free_time > other.next_free_time

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i])

    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        next_free_time = [0] * self.num_workers
        for i in range(len(self.jobs)):
          next_worker = 0
          for j in range(self.num_workers):
            if next_free_time[j] < next_free_time[next_worker]:
              next_worker = j
          self.assigned_workers[i] = next_worker
          self.start_times[i] = next_free_time[next_worker]
          next_free_time[next_worker] += self.jobs[i]

    def fast_assign_jobs(self):
        self.workers_queue = [Worker(i) for i in range(self.num_workers)]
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        for i in range(len(self.jobs)):
          next_worker = self.workers_queue[0]
          self.assigned_workers[i] = next_worker.id
          self.start_times[i] = next_worker.next_free_time
          next_worker.next_free_time += self.jobs[i]
          self.siftdown(0)

    def siftdown(self, i):
        p_worker = self.workers_queue[i]
        l_child = 2 * i + 1
        r_child = 2 * i + 2
        #l_child_worker = self.workers_queue[l_child]
        #r_child_worker = self.workers_queue[r_child]
        min_index = i
        if l_child < self.num_workers and self.workers_queue[min_index].is_larger(self.workers_queue[l_child]):
          min_index = l_child
        if r_child < self.num_workers and self.workers_queue[min_index].is_larger(self.workers_queue[r_child]):
          min_index = r_child
        if i != min_index:
          self.workers_queue[min_index], self.workers_queue[i] = self.workers_queue[i], self.workers_queue[min_index]
          self.siftdown(min_index)

    def solve(self):
        self.read_data()
        self.fast_assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

