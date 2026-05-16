-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 11, 2026 at 09:58 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mobila_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `cart_tb`
--

CREATE TABLE `cart_tb` (
  `c_id` int(11) NOT NULL,
  `o_id` int(11) NOT NULL,
  `p_id` int(11) NOT NULL,
  `c_price` int(11) NOT NULL,
  `c_quantity` int(11) NOT NULL,
  `c_totalprice` int(11) NOT NULL,
  `c_status` enum('Active','Deactive') NOT NULL,
  `c_cdate` datetime NOT NULL,
  `c_udate` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `category_tb`
--

CREATE TABLE `category_tb` (
  `cat_id` int(11) NOT NULL,
  `cat_name` varchar(50) NOT NULL,
  `cat_image` varchar(100) NOT NULL,
  `cat_status` enum('Active','Deactive') NOT NULL,
  `cat_cdate` datetime NOT NULL,
  `cat_udate` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `category_tb`
--

INSERT INTO `category_tb` (`cat_id`, `cat_name`, `cat_image`, `cat_status`, `cat_cdate`, `cat_udate`) VALUES
(8, 'IPHONE', 'APPLE_AG54Mzf.jpeg', 'Active', '2026-01-04 10:30:12', '2026-01-04 10:30:12'),
(9, 'SAMSUNG', 'SAM-LOGOD_hqySYao.png', 'Active', '2026-01-04 10:30:28', '2026-01-04 10:30:28'),
(10, 'IQOO', 'iqoo_2KbzZoV.png', 'Active', '2026-01-04 10:30:43', '2026-01-04 10:30:43'),
(11, 'XIAOMI', 'xiaomi_knMCv85.png', 'Active', '2026-01-04 10:30:55', '2026-01-04 10:30:55'),
(12, 'VIVO', 'vivo_UzLonmm.avif', 'Active', '2026-01-04 10:31:11', '2026-01-04 10:31:11');

-- --------------------------------------------------------

--
-- Table structure for table `feedback_tb`
--

CREATE TABLE `feedback_tb` (
  `f_id` int(11) NOT NULL,
  `f_name` varchar(50) NOT NULL,
  `f_contact` bigint(20) NOT NULL,
  `f_message` text NOT NULL,
  `f_status` enum('Active','Deactive') NOT NULL,
  `f_cdate` datetime NOT NULL,
  `f_udate` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `feedback_tb`
--

INSERT INTO `feedback_tb` (`f_id`, `f_name`, `f_contact`, `f_message`, `f_status`, `f_cdate`, `f_udate`) VALUES
(1, 'kunj', 9904893718, '“Great experience! I bought my phone here at a very reasonable price. Staff is friendly and explained all features clearly.”', 'Active', '2026-02-09 15:08:31', '2026-02-09 15:08:31'),
(2, 'Preya', 9909966066, '“Best mobile shop in the area. 100% original products and fast service. I’m very satisfied with my purchase.”', 'Active', '2026-02-09 15:09:11', '2026-02-09 15:09:11'),
(3, 'Foram', 9874563210, '“Wide variety of mobiles and accessories. I got a good exchange offer and the process was smooth.”', 'Active', '2026-02-09 15:10:05', '2026-02-09 15:10:05'),
(4, 'Prince ', 9099740772, '“Trustworthy shop with best prices. After-sales service is very good. Highly recommended!”', 'Deactive', '2026-02-09 21:53:07', '2026-02-09 21:53:07');

-- --------------------------------------------------------

--
-- Table structure for table `login_tb`
--

CREATE TABLE `login_tb` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `image` varchar(100) NOT NULL,
  `lastseen` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `login_tb`
--

INSERT INTO `login_tb` (`id`, `username`, `password`, `image`, `lastseen`) VALUES
(1, 'admin', '2210', 'p_logo.jpg', '2026-02-11 13:54:40');

-- --------------------------------------------------------

--
-- Table structure for table `order_tb`
--

CREATE TABLE `order_tb` (
  `o_id` int(11) NOT NULL,
  `u_id` int(11) NOT NULL,
  `o_pincode` int(11) DEFAULT NULL,
  `o_address` text DEFAULT NULL,
  `o_totalquntity` int(11) NOT NULL,
  `o_totalprice` int(11) NOT NULL,
  `o_status` enum('Cart','Pending','Confirm','Complete','Cancel') NOT NULL,
  `o_cdate` datetime NOT NULL,
  `o_udate` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `product_tb`
--

CREATE TABLE `product_tb` (
  `p_id` int(11) NOT NULL,
  `cat_id` int(11) NOT NULL,
  `p_name` varchar(100) NOT NULL,
  `p_mrp` int(10) NOT NULL,
  `p_price` int(10) NOT NULL,
  `p_details` text NOT NULL,
  `p_img1` varchar(100) NOT NULL,
  `p_img2` varchar(100) NOT NULL,
  `p_img3` varchar(100) NOT NULL,
  `p_descleminar` text NOT NULL,
  `p_status` enum('Active','Deactive') NOT NULL,
  `p_cdate` datetime NOT NULL,
  `p_udate` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `product_tb`
--

INSERT INTO `product_tb` (`p_id`, `cat_id`, `p_name`, `p_mrp`, `p_price`, `p_details`, `p_img1`, `p_img2`, `p_img3`, `p_descleminar`, `p_status`, `p_cdate`, `p_udate`) VALUES
(6, 8, 'Iphone 14 Pro', 71000, 61000, 'Apple Iphone 14 Pro Blue Finishing', 'Iphone 14 Pro.jpg', 'Iphone 14 Pro.jpg', 'Iphone 14 Pro.jpg', 'Good Product Quality', 'Active', '2025-12-27 09:34:14', '2025-12-27 09:34:14'),
(7, 12, 'vivo v18 pro ', 71000, 61000, 'Good quality ', 'Iphone 14 Pro.jpg', 'Iphone 14 Pro.jpg', 'Iphone 14 Pro.jpg', 'Available ', 'Active', '2025-12-29 09:12:29', '2025-12-29 09:12:29'),
(8, 8, 'Iphone 14 Pro', 199999, 187989, 'Apple – iPhone 14 Pro Max 128GB – Deep Purple (Verizon)', 'Iphone 14 Pro_ZAUQv6C.jpg', 'ip 14 -1_VJ0PoOw.jpg', 'ip 14 -2_izfyA1B.jpg', 'Limited stock', 'Deactive', '2026-01-04 10:35:03', '2026-02-09 21:18:01'),
(9, 8, 'iphone 15', 74799, 69999, 'Apple iPhone 15 (512 GB) - Pink ', 'ip 15 2.1_gZDpQ98.jpg', 'ip 15 2_Wbpsbdi.jpg', 'ip 15 2.2_4wbpijM.jpg', 'Good Product Quality', 'Active', '2026-01-04 10:40:48', '2026-01-04 10:41:10'),
(10, 8, 'Iphone 17 Pro Max', 154999, 145899, 'iPhone 17 Pro 256 GB: 15.93 cm (6.3″) Display with Promotion up to 120Hz, A19 Pro Chip, Breakthrough Battery Life, Pro Fusion Camera System with Center Stage Front Camera; Deep Blue', 'ip 17_EIdrTes.jpg', 'ip 17.1_fOlQSNa.jpg', 'ip 17.2_V9E9k3x.jpg', 'Premium Quality ', 'Active', '2026-01-04 10:45:14', '2026-01-04 10:45:14'),
(11, 8, 'Iphone 16', 70999, 66299, 'iPhone 16 128 GB: 5G Mobile Phone with Camera Control, A18 Chip and a Big Boost in Battery Life. Works with AirPods; Teal', 'ip 16.1_EbjI2Vz.jpg', 'ip 16_3c40IW6.webp', 'ip 16.2_GT15OTa.jpg', 'Good', 'Active', '2026-01-04 10:51:30', '2026-01-04 10:51:30'),
(12, 8, 'Iphone Air', 68999, 62299, 'iPhone 16 128 GB: 5G Mobile Phone with Camera Control, A18 Chip and a Big Boost in Battery Life. Works with AirPods; Tea', 'ip 16 e_h7Lps0z.jpg', 'ip 16 e 1_Ry6E1rf.jpg', 'ip 16 e 3_NkZScPy.jpg', 'Good Perfomance', 'Active', '2026-01-04 10:58:01', '2026-01-04 10:58:01'),
(13, 9, 'Samsung Galaxy A55 5G', 60599, 52499, 'Samsung Galaxy A55 5G (Awesome Iceblue, 8GB RAM, 256GB Storage) | AI | Metal Frame | 50 MP Main Camera (OIS) | Super HDR Video| Nightography | IP67 | Corning Gorilla Glass Victus+ | sAMOLED Display\r\n', 'sam a55 0_pvZ9nYw.jpg', 'sam a55 1_vcyY5jK.jpg', 'sam a55 2_Qf41W4S.jpg', 'Good ', 'Active', '2026-01-04 11:15:57', '2026-01-04 11:15:57'),
(14, 9, 'Samsung Galaxy S25 Ultra 5G AI', 168999, 162499, 'Samsung Galaxy S25 Ultra 5G AI Smartphone (Titanium Silverblue, 12GB RAM, 512GB Storage), 200MP Camera, S Pen Included, Long Battery Life\r\n', 'sam 25 ultra 0_yBPft6P.webp', 'sam 25 ultra 2_yeg7Dl1.jpeg', 'sam 25 ultra 1_usL6lEu.jpeg', 'Premium Quality', 'Active', '2026-01-04 11:17:43', '2026-01-04 11:17:43'),
(15, 9, 'Samsung Galaxy S24 Ultra 5G AI', 162999, 154499, 'Samsung Galaxy S24 Ultra 5G AI Smartphone with Galaxy AI (Titanium Black, 12GB, 512GB Storage), Snapdragon 8 Gen 3, 200 MP Camera with ProVisual Engine and 5000mAh Battery\r\n', 'sam 24 ultra 0_QBw53Nw.webp', 'sam 24 ultra 3_VDViyPj.jpeg', 'sam 24 ulta 1_jdHvnDK.jpg', 'Unbeatable  Performance ', 'Active', '2026-01-04 11:20:11', '2026-01-04 11:20:11'),
(16, 9, 'Samsung Galaxy A56 5G ', 54599, 48569, 'Samsung Galaxy A56 5G (Awesome Olive, 12GB, 256GB) | Metal Frame | Gemini Live | Awesome Intelligence (AI): Circle to Search, Instant Slo-Mo, Auto-Trim, Object Eraser | Flagship Grade Camera\r\n', 'sam a55 0_vOpiRvp.jpg', 'sam a55 2_Iofvkvn.jpg', 'sam a55 1_vcyY5jK_UvlcCjM.jpg', 'Good ', 'Active', '2026-01-04 11:21:46', '2026-01-04 11:21:46'),
(17, 9, 'Samsung Galaxy Z Flip5 5G AI', 70499, 66599, 'Samsung Galaxy Z Flip5 5G AI Smartphone (Graphite, 8GB RAM, 256GB Storage)\r\n', 'sam z filp  0_OEbXM21.jpg', 'sam z flip 2_FNEAObn.jpg', 'sam flip 2_giGjvT9.jpg', 'Very HIgh Performance ', 'Active', '2026-01-04 11:23:42', '2026-01-04 11:23:42'),
(18, 10, 'iQOO 15', 84599, 81199, 'iQOO 15 (Legend, 12GB RAM, 256GB Storage) | Fastest Snapdragon 8 Elite Gen 5 Processor* | Origin OS 6 - Out of The Box* | Samsung 2K M14 Lead OLED Display | Aditional Exchange Offers\r\n', 'iqoo 15 0_9SxmyzG.jpeg', 'iqoo 15 2_VzwrWEO.jpg', 'iqoo 15 1_OJTczvU.jpg', 'High Perfomance', 'Active', '2026-01-04 11:59:56', '2026-01-04 11:59:56'),
(19, 10, 'iQOO Neo 10', 35799, 25699, 'iQOO Neo 10 (Inferno Red, 16GB RAM, 512GB Storage) | Snapdragon 8s Gen 4 Processor & SuperComputing Chip Q1 | 7000 mAh Battery | Segment’s Highest 144 FPS Gaming Smartphone\r\n', 'iqoo  neo10 0_8w6lmtb.jpg', 'iqoo neo 1_wSaZXkW.jpg', 'iqoo neo 2_iQG5YT8.jpg', 'Good', 'Active', '2026-01-04 12:05:56', '2026-01-04 12:05:56'),
(20, 10, 'IQOO Z7 Pro 5G', 40599, 32299, 'IQOO Z7 Pro 5G (Blue Lagoon, 256 GB)  (16 GB RAM)\r\n', 'iqoo z7 p 0_U9VpArT.jpeg', 'iqoo z7 p 2_8eLXMc5.png', 'iqoo z7 p 1_GXKwR2z.jpeg', 'Unbeatable Performance', 'Active', '2026-01-04 12:08:55', '2026-01-05 14:42:18'),
(21, 10, 'iQOO Neo 10R 5G ', 61599, 51599, 'iQOO Neo 10R 5G (Moonknight Titanium, 8GB RAM, 256GB Storage) | Snapdragon 8s Gen 3 Processor | India\'s Slimmest 6400mAh Battery Smartphone\r\n', 'iqoo  neo10 0.jpg', 'iqoo neo 1.jpg', 'iqoo neo 2.jpg', 'Good', 'Active', '2026-01-04 07:45:12', '2026-01-04 07:45:12'),
(22, 10, 'iQOO 13 Pro  ', 75999, 69999, 'Display: 6.8″ QHD+ AMOLED, 144Hz,Processor: Snapdragon 8 Gen series (flagship),RAM / Storage: 12GB / 16GB RAM, up to 1TB storage\r\n,Rear Camera: 50MP (Main) + 50MP (Ultra-wide) + Telephoto', 'iqoo 13 pro 1_wbmBOEw.jpeg', 'iqoo 13 pro 2_qFWLH3Z.jpeg', 'iqoo 13 pro 3_YcRI43u.jpeg', 'Goood', 'Active', '2026-01-04 15:16:58', '2026-01-04 15:16:58'),
(23, 10, 'iQOO Z10R 5G ', 49599, 45299, 'iQOO Z10R 5G (Aquamarine, 12GB RAM, 256GB Storage) | 32MP 4K Selfie Camera | Quad-Curved AMOLED Display | Dimensity 7400 Processor with 750K+ AnTuTu Score\r\n', 'iqoo z10 r 0_TYntzvq.webp', 'iqoo z10 r 1_9CSnsUv.jpg', 'iqoo z10 r 2_8WjCaaL.jpg', 'Cool ', 'Active', '2026-01-04 15:20:08', '2026-01-04 15:20:08'),
(24, 12, 'vivo V60e 5G ', 32999, 28999, 'vivo V60e 5G (Noble Gold, 8GB RAM, 256GB Storage) with No Cost EMI/Additional Exchange Offers\r\n', 'vivo v 60.0_u36ivNP.jpg', 'vivo v 60.1_N1W55r6.jpg', 'vivo v 60.2_Cj0k7Tt.jpg', 'Good', 'Active', '2026-01-04 16:00:38', '2026-01-04 16:00:38'),
(25, 12, 'vivo T4R 5G', 28450, 23599, 'vivo T4R 5G (Twilight Blue, 256 GB) (12 GB RAM)\r\n', 'vivo t4 t1_yj995kr.webp', 'vivo t4.2_Kv66CY8.jpg', 'vivo t4.36_h632GUC.jpg', 'Good', 'Active', '2026-01-04 16:08:02', '2026-02-09 21:44:46'),
(26, 12, ' vivo X300 5G', 79599, 72999, 'vivo X300 5G (Elite Black, 12GB RAM, 256GB Storage) with No Cost EMI/Additional Exchange Offers\r\n', 'vivo x300.0_j9refIr.jpg', 'vivo x 300.1_h0t7xrm.jpg', 'vivo x300.2_dZraCiA.jpg', 'Unbeatable Performance ', 'Active', '2026-01-04 16:10:12', '2026-01-04 16:10:12'),
(27, 12, ' Vivo T4x 5G', 25999, 21599, 'Vivo T4x 5G (Marine Blue, 128 GB) (6 GB RAM)\r\n', 'vivo t4x.1_GlcjDpn.jpg', 'vivo t4x.2_sGl9uub.jpg', 'vivo t4x.3_9zNes5k.jpg', 'Good', 'Active', '2026-01-04 16:11:30', '2026-01-04 16:11:30'),
(28, 12, 'Vivo Y19e', 18999, 16999, 'Vivo Y19e (Titanium Silver, 4GB RAM, 64GB Storage) with No Cost EMI/Additional Exchange Offers |with Charger\r\n', 'Vivo Y19e.1_Ff7h0fE.jpg', 'Vivo Y19e.2_tLaORIc.jpg', 'Vivo Y19e.3_M5TsIy8.jpg', 'Good', 'Active', '2026-01-04 16:12:44', '2026-01-04 16:12:44'),
(29, 11, 'XIAOMI 14 Civi ', 50499, 45899, 'XIAOMI 14 Civi Matcha Green (8GB RAM 256GB Storage) | 50 MP Leica Triple Camera| SD 8s Gen 3 | 1.5K Quad Curved AMOLED HyperOS\r\n', 'x 14.1_objUgr0.jpg', 'x 14.2_sWTgur1.jpg', 'x 14.3_VmR0epd.jpg', 'Very Good Performance ', 'Active', '2026-01-04 16:14:15', '2026-01-04 16:14:15'),
(30, 11, 'XIAOMI 14 ', 75999, 67599, 'XIAOMI 14 (White, 12GB RAM, 512GB Storage) | 50MP Leica Professional Optics | 120 Hz 1.5K LTPO AMOLED | SD 8 Gen 3 Hyper OS\r\n', 'XIAOMI 14.0_fPM5sOE.jpg', 'XIAOMI 14.1_eKqXWOG.jpg', 'XIAOMI 14.3_LDQuPMq.jpg', 'Very High Processor ', 'Active', '2026-01-04 16:19:51', '2026-02-09 21:19:25'),
(31, 11, 'Redmi 15 5G', 35999, 31999, 'Redmi 15 5G Sandy Purple 256GB ,  7000mAhA Battery , Display 17.53cm Up to 144Hz , Snapdragon 6s Gen 3 , 18W Reverse Charging , 50MP AI Dual Camera\r\n', 'x redmi 15.0_D8vcElE.webp', 'x redmi 15.1_l3dTxTB.jpg', 'x redmi 15.2_woCsLtK.jpg', 'Good', 'Active', '2026-01-05 14:31:42', '2026-01-05 14:33:36'),
(32, 11, 'Redmi Note 13 Pro', 42999, 36899, 'The Redmi Note 13 Pro captures excellent 4K video with its 200MP main camera, offering great detail, stabilization, and dynamic range, especially in good lighting, while also providing 2x lossless zoom for closer shots\r\n', 'x redmi 13 p.0_eDrXbxV.jpeg', 'x redmi 13 p.2_Zr0QhCd.jpeg', 'x redmi 13 p.1_VjmFQf5.jpeg', 'Very High Perfomance', 'Active', '2026-01-05 14:37:02', '2026-02-09 21:20:01'),
(33, 11, 'Redmi Note 14 5G', 85599, 79499, 'Redmi Note 14 5G ,Titan Black, 6GB RAM 128GB Storage , Global Debut MTK Dimensity 7025 Ultra , 2100 nits Segment Brightest 120Hz AMOLED , 50MP Sony LYT 600 OIS+EIS Triple Camera\r\n', 'x redmi not 15.0_EY8cuPY.jpg', 'x redmi not 15.1_OsPT3x4.jpg', 'x redmi not 15.2_6qTkDFM.jpg', 'Excellent ', 'Active', '2026-01-05 14:41:30', '2026-02-09 21:19:48');

-- --------------------------------------------------------

--
-- Table structure for table `user_tb`
--

CREATE TABLE `user_tb` (
  `u_id` int(11) NOT NULL,
  `u_name` varchar(50) NOT NULL,
  `u_contact` bigint(20) NOT NULL,
  `u_address` text NOT NULL,
  `u_img` varchar(100) NOT NULL,
  `u_password` varchar(20) NOT NULL,
  `u_status` enum('Active','Deactive') NOT NULL,
  `u_cdate` datetime NOT NULL,
  `u_udate` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user_tb`
--

INSERT INTO `user_tb` (`u_id`, `u_name`, `u_contact`, `u_address`, `u_img`, `u_password`, `u_status`, `u_cdate`, `u_udate`) VALUES
(4, 'Kunj Ladani', 9904893718, 'Gandhinagar Sector-15 ', 'IMG_20231022_101045.jpg', '2210', 'Active', '2026-01-26 12:39:33', '2026-02-11 13:54:47'),
(5, 'Prince', 9099740772, 'Gandhinagar', 'vjv.png', '2342', 'Active', '2026-01-27 15:41:25', '2026-01-27 15:41:25'),
(7, 'Preya Patel', 9227153104, 'Gandhinagar Sector 15 ', 'sign.jpg', '2210', 'Active', '2026-02-09 14:55:19', '2026-02-09 14:55:19');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cart_tb`
--
ALTER TABLE `cart_tb`
  ADD PRIMARY KEY (`c_id`);

--
-- Indexes for table `category_tb`
--
ALTER TABLE `category_tb`
  ADD PRIMARY KEY (`cat_id`);

--
-- Indexes for table `feedback_tb`
--
ALTER TABLE `feedback_tb`
  ADD PRIMARY KEY (`f_id`);

--
-- Indexes for table `login_tb`
--
ALTER TABLE `login_tb`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `order_tb`
--
ALTER TABLE `order_tb`
  ADD PRIMARY KEY (`o_id`);

--
-- Indexes for table `product_tb`
--
ALTER TABLE `product_tb`
  ADD PRIMARY KEY (`p_id`);

--
-- Indexes for table `user_tb`
--
ALTER TABLE `user_tb`
  ADD PRIMARY KEY (`u_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `cart_tb`
--
ALTER TABLE `cart_tb`
  MODIFY `c_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `category_tb`
--
ALTER TABLE `category_tb`
  MODIFY `cat_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `feedback_tb`
--
ALTER TABLE `feedback_tb`
  MODIFY `f_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `login_tb`
--
ALTER TABLE `login_tb`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `order_tb`
--
ALTER TABLE `order_tb`
  MODIFY `o_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `product_tb`
--
ALTER TABLE `product_tb`
  MODIFY `p_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT for table `user_tb`
--
ALTER TABLE `user_tb`
  MODIFY `u_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
