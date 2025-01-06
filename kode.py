from metaflow import FlowSpec, step

class KuliahInformatika(FlowSpec):
    @step
    def start(self):
        print("Langkah-langkah mengikuti kuliah di Informatika")
        self.next(self.bayar_spp)
    
    @step
    def bayar_spp(self):
        print("1. Membayar SPP keuangan semester")
        self.next(self.pengisian_krs)

    @step
    def pengisian_krs(self):
        print("2. Mengisi Kartu Rencana Studi (KRS)")
        self.next(self.presensi_kuliah)
    
    @step
    def presensi_kuliah(self):
        print("3. Mengikuti perkuliahan dan melakukan presensi")
        self.next(self.ujian_akhir)
    
    @step
    def ujian_akhir(self):
        print("4. Mengikuti ujian akhir semester")
        self.next(self.dapat_khs)
    
    @step
    def dapat_khs(self):
        print("5. Mendapatkan Kartu Hasil Studi (KHS)")
        self.next(self.end)
    
    @step
    def end(self):
        print("Proses mengikuti kuliah selesai")
    
if __name__ == '__main__':

    KuliahInformatika()