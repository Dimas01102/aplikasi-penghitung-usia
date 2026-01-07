import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from typing import Tuple, Optional
import calendar


class AplikasiPenghitungUsia:
    """Class utama untuk aplikasi penghitung usia"""
    
    # Konstanta untuk zodiak
    ZODIAK = {
        "Capricorn": [(12, 22), (1, 19)],
        "Aquarius": [(1, 20), (2, 18)],
        "Pisces": [(2, 19), (3, 20)],
        "Aries": [(3, 21), (4, 19)],
        "Taurus": [(4, 20), (5, 20)],
        "Gemini": [(5, 21), (6, 20)],
        "Cancer": [(6, 21), (7, 22)],
        "Leo": [(7, 23), (8, 22)],
        "Virgo": [(8, 23), (9, 22)],
        "Libra": [(9, 23), (10, 22)],
        "Scorpio": [(10, 23), (11, 21)],
        "Sagittarius": [(11, 22), (12, 21)]
    }
    
    def __init__(self, root):
        """Inisialisasi aplikasi"""
        self.root = root
        self.setup_window()
        self.create_widgets()
        
    def setup_window(self):
        """Konfigurasi jendela utama"""
        self.root.title("Aplikasi Penghitung Usia")
        self.root.geometry("650x700")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f4f8")
        self.center_window()
        
    def center_window(self):
        """Menempatkan window di tengah layar"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
    def create_widgets(self):
        """Membuat semua widget GUI"""
        main_frame = tk.Frame(self.root, bg="#f0f4f8")
        main_frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        self.create_header(main_frame)
        self.create_input_section(main_frame)
        self.create_button(main_frame)
        self.create_result_section(main_frame)
        
    def create_header(self, parent):
        """Membuat header aplikasi"""
        header_frame = tk.Frame(parent, bg="#2c3e50", relief="raised", bd=2)
        header_frame.pack(fill="x", pady=(0, 20))
        
        icon_label = tk.Label(header_frame, text="🎂", font=("Arial", 40), 
                            bg="#2c3e50", fg="white")
        icon_label.pack(pady=(10, 5))
        
        title_label = tk.Label(header_frame, text="APLIKASI PENGHITUNG USIA",
                              font=("Arial", 20, "bold"), bg="#2c3e50", fg="white")
        title_label.pack(pady=(0, 5))
        
        subtitle_label = tk.Label(header_frame, text="Hitung usia Anda dengan akurat",
                                 font=("Arial", 10), bg="#2c3e50", fg="#ecf0f1")
        subtitle_label.pack(pady=(0, 10))
        
    def create_input_section(self, parent):
        """Membuat section input tanggal lahir"""
        input_frame = tk.LabelFrame(parent, text=" 📅 Masukkan Tanggal Lahir ",
                                   font=("Arial", 12, "bold"), bg="#ffffff",
                                   fg="#2c3e50", relief="groove", bd=2,
                                   padx=20, pady=20)
        input_frame.pack(fill="x", pady=(0, 20))
        
        fields_container = tk.Frame(input_frame, bg="#ffffff")
        fields_container.pack()
        
        # Tanggal
        self.create_input_field(fields_container, "Tanggal:", 0,
                              list(range(1, 32)), "tanggal")
        
        # Bulan
        bulan_list = ["Januari", "Februari", "Maret", "April", "Mei", "Juni",
                     "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
        self.create_input_field(fields_container, "Bulan:", 1, bulan_list, "bulan")
        
        # Tahun
        tahun_sekarang = datetime.now().year
        tahun_list = list(range(tahun_sekarang, tahun_sekarang - 120, -1))
        self.create_input_field(fields_container, "Tahun:", 2, tahun_list, "tahun")
        
    def create_input_field(self, parent, label_text, row, values, attr_name):
        """Membuat field input dengan combobox"""
        label = tk.Label(parent, text=label_text, font=("Arial", 11, "bold"),
                        bg="#ffffff", fg="#34495e")
        label.grid(row=row, column=0, sticky="w", pady=10, padx=(0, 10))
        
        combo = ttk.Combobox(parent, values=values, state="readonly",
                           font=("Arial", 11), width=25)
        combo.grid(row=row, column=1, pady=10)
        combo.set(f"-- Pilih {label_text.strip(':')} --")
        
        setattr(self, f"combo_{attr_name}", combo)
        
    def create_button(self, parent):
        """Membuat tombol hitung dan reset"""
        button_frame = tk.Frame(parent, bg="#f0f4f8")
        button_frame.pack(pady=10)
        
        hitung_btn = tk.Button(button_frame, text="🔢 HITUNG USIA",
                              font=("Arial", 12, "bold"), bg="#27ae60", fg="white",
                              activebackground="#229954", activeforeground="white",
                              cursor="hand2", width=20, height=2, relief="raised",
                              bd=3, command=self.hitung_usia)
        hitung_btn.pack(side="left", padx=5)
        
        reset_btn = tk.Button(button_frame, text="🔄 RESET",
                             font=("Arial", 12, "bold"), bg="#e74c3c", fg="white",
                             activebackground="#c0392b", activeforeground="white",
                             cursor="hand2", width=20, height=2, relief="raised",
                             bd=3, command=self.reset_form)
        reset_btn.pack(side="left", padx=5)
        
    def create_result_section(self, parent):
        """Membuat section hasil perhitungan"""
        result_frame = tk.LabelFrame(parent, text=" 📊 Hasil Perhitungan ",
                                    font=("Arial", 12, "bold"), bg="#ffffff",
                                    fg="#2c3e50", relief="groove", bd=2,
                                    padx=20, pady=20)
        result_frame.pack(fill="both", expand=True)
        
        self.result_text = tk.Text(result_frame, font=("Courier New", 11),
                                  bg="#ecf0f1", fg="#2c3e50", relief="sunken",
                                  bd=2, wrap="word", height=15, padx=15, pady=15)
        self.result_text.pack(fill="both", expand=True)
        
        scrollbar = tk.Scrollbar(self.result_text)
        scrollbar.pack(side="right", fill="y")
        self.result_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.result_text.yview)
        
        self.result_text.config(state="disabled")
        self.display_initial_message()
        
    def display_initial_message(self):
        """Menampilkan pesan awal"""
        message = """
╔════════════════════════════════════════════════╗
║                                                ║
║       Silakan masukkan tanggal lahir Anda      ║
║         kemudian klik tombol HITUNG            ║
║                                                ║
╚════════════════════════════════════════════════╝

ℹ️  Informasi yang akan ditampilkan:
   • Usia dalam tahun, bulan, dan hari
   • Total hari hidup
   • Hari ulang tahun berikutnya
   • Zodiak berdasarkan tanggal lahir
        """
        self.result_text.config(state="normal")
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(1.0, message)
        self.result_text.config(state="disabled")
        
    def validasi_input(self) -> Tuple[bool, Optional[datetime], Optional[str]]:
        """Validasi input dari user"""
        try:
            tanggal_str = self.combo_tanggal.get()
            bulan_str = self.combo_bulan.get()
            tahun_str = self.combo_tahun.get()
            
            if tanggal_str.startswith("--") or bulan_str.startswith("--") or tahun_str.startswith("--"):
                return False, None, "Semua field harus diisi!"
            
            bulan_dict = {
                "Januari": 1, "Februari": 2, "Maret": 3, "April": 4,
                "Mei": 5, "Juni": 6, "Juli": 7, "Agustus": 8,
                "September": 9, "Oktober": 10, "November": 11, "Desember": 12
            }
            
            tanggal = int(tanggal_str)
            bulan = bulan_dict[bulan_str]
            tahun = int(tahun_str)
            
            max_hari = calendar.monthrange(tahun, bulan)[1]
            if tanggal > max_hari:
                return False, None, f"Tanggal {tanggal} tidak valid untuk bulan {bulan_str}!"
            
            tanggal_lahir = datetime(tahun, bulan, tanggal)
            
            if tanggal_lahir > datetime.now():
                return False, None, "Tanggal lahir tidak boleh di masa depan!"
            
            return True, tanggal_lahir, None
            
        except ValueError as e:
            return False, None, f"Format tanggal tidak valid: {str(e)}"
        except Exception as e:
            return False, None, f"Terjadi kesalahan: {str(e)}"
    
    def hitung_detail_usia(self, tanggal_lahir: datetime) -> dict:
        """Menghitung detail usia dari tanggal lahir"""
        hari_ini = datetime.now()
        
        tahun = hari_ini.year - tanggal_lahir.year
        bulan = hari_ini.month - tanggal_lahir.month
        hari = hari_ini.day - tanggal_lahir.day
        
        if hari < 0:
            bulan -= 1
            bulan_sebelum = hari_ini.month - 1 if hari_ini.month > 1 else 12
            tahun_bulan_sebelum = hari_ini.year if hari_ini.month > 1 else hari_ini.year - 1
            hari_dalam_bulan = calendar.monthrange(tahun_bulan_sebelum, bulan_sebelum)[1]
            hari += hari_dalam_bulan
        
        if bulan < 0:
            tahun -= 1
            bulan += 12
        
        total_hari = (hari_ini - tanggal_lahir).days
        
        ultah_tahun_ini = datetime(hari_ini.year, tanggal_lahir.month, tanggal_lahir.day)
        if ultah_tahun_ini < hari_ini:
            ultah_berikutnya = datetime(hari_ini.year + 1, tanggal_lahir.month, tanggal_lahir.day)
        else:
            ultah_berikutnya = ultah_tahun_ini
        
        hari_ke_ultah = (ultah_berikutnya - hari_ini).days
        zodiak = self.tentukan_zodiak(tanggal_lahir.month, tanggal_lahir.day)
        
        return {
            "tahun": tahun, "bulan": bulan, "hari": hari,
            "total_hari": total_hari, "hari_ke_ultah": hari_ke_ultah,
            "tanggal_ultah": ultah_berikutnya, "zodiak": zodiak
        }
    
    def tentukan_zodiak(self, bulan: int, hari: int) -> str:
        """Menentukan zodiak berdasarkan tanggal lahir"""
        for nama_zodiak, rentang in self.ZODIAK.items():
            if len(rentang) == 2:
                (bulan1, hari1), (bulan2, hari2) = rentang
                if bulan == bulan1 and hari >= hari1:
                    return nama_zodiak
                elif bulan == bulan2 and hari <= hari2:
                    return nama_zodiak
        return "Unknown"
    
    def format_hasil(self, detail: dict, tanggal_lahir: datetime) -> str:
        """Format hasil perhitungan"""
        bulan_nama = ["Januari", "Februari", "Maret", "April", "Mei", "Juni",
                     "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
        
        tgl_lahir_str = f"{tanggal_lahir.day} {bulan_nama[tanggal_lahir.month-1]} {tanggal_lahir.year}"
        tgl_ultah_str = f"{detail['tanggal_ultah'].day} {bulan_nama[detail['tanggal_ultah'].month-1]} {detail['tanggal_ultah'].year}"
        
        simbol_zodiak = {
            "Capricorn": "♑", "Aquarius": "♒", "Pisces": "♓", "Aries": "♈",
            "Taurus": "♉", "Gemini": "♊", "Cancer": "♋", "Leo": "♌",
            "Virgo": "♍", "Libra": "♎", "Scorpio": "♏", "Sagittarius": "♐"
        }
        
        hasil = f"""
╔════════════════════════════════════════════════╗
║           HASIL PERHITUNGAN USIA               ║
╚════════════════════════════════════════════════╝

📅 TANGGAL LAHIR
   {tgl_lahir_str}

🎂 USIA ANDA SAAT INI
   ├─ {detail['tahun']} Tahun
   ├─ {detail['bulan']} Bulan
   └─ {detail['hari']} Hari

📊 DETAIL LENGKAP
   • Total Hari Hidup    : {detail['total_hari']:,} hari
   • Hari ke Ulang Tahun : {detail['hari_ke_ultah']} hari lagi
   • Tanggal Ulang Tahun : {tgl_ultah_str}

⭐ ZODIAK ANDA
   {detail['zodiak']} {simbol_zodiak.get(detail['zodiak'], '')}

╔════════════════════════════════════════════════╗
║  Terima kasih telah menggunakan aplikasi ini!  ║
╚════════════════════════════════════════════════╝
        """
        return hasil
    
    def hitung_usia(self):
        """Method utama untuk menghitung usia"""
        is_valid, tanggal_lahir, error_msg = self.validasi_input()
        
        if not is_valid:
            messagebox.showerror("Error Validasi", error_msg)
            return
        
        try:
            detail = self.hitung_detail_usia(tanggal_lahir)
            hasil = self.format_hasil(detail, tanggal_lahir)
            
            self.result_text.config(state="normal")
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(1.0, hasil)
            self.result_text.config(state="disabled")
            
            messagebox.showinfo("Perhitungan Berhasil",
                f"Usia Anda: {detail['tahun']} Tahun, {detail['bulan']} Bulan, {detail['hari']} Hari")
            
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan:\n{str(e)}")
    
    def reset_form(self):
        """Reset semua input dan hasil"""
        self.combo_tanggal.set("-- Pilih Tanggal --")
        self.combo_bulan.set("-- Pilih Bulan --")
        self.combo_tahun.set("-- Pilih Tahun --")
        self.display_initial_message()
        messagebox.showinfo("Reset", "Form telah direset!")


def main():
    """Fungsi utama untuk menjalankan aplikasi"""
    root = tk.Tk()
    app = AplikasiPenghitungUsia(root)
    root.mainloop()


if __name__ == "__main__":
    main()
