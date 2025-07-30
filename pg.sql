-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 02, 2024 at 08:30 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pg`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(5) NOT NULL,
  `name` varchar(10) NOT NULL DEFAULT 'admin',
  `password` varchar(20) NOT NULL DEFAULT '123456'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `name`, `password`) VALUES
(1, 'admin', '123456');

-- --------------------------------------------------------

--
-- Table structure for table `pg_details`
--

CREATE TABLE `pg_details` (
  `id` int(11) NOT NULL,
  `pg_name` varchar(100) NOT NULL,
  `pg_address` varchar(100) NOT NULL,
  `pg_rent` int(5) NOT NULL,
  `pg_amenities` varchar(100) NOT NULL,
  `pg_type` varchar(11) NOT NULL,
  `pg_owner_id` bigint(10) NOT NULL,
  `pg_image` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pg_details`
--

INSERT INTO `pg_details` (`id`, `pg_name`, `pg_address`, `pg_rent`, `pg_amenities`, `pg_type`, `pg_owner_id`, `pg_image`) VALUES
(2, 'New PG', 'Jalandhar Bus stand', 5000, 'Wifi, AC', 'Boys', 9876543210, 'uploaded_files\\entry.jpeg'),
(3, 'Student PG', 'Mithapur,jalandhar', 4000, 'AC', 'Boys', 8990989001, 'uploaded_files\\sign.png'),
(4, 'PG Rooms', 'Jalandhar Bus stand', 6000, 'wifi, AC', 'Boys', 8968901234, 'uploaded_files\\pglogo.png'),
(5, 'PGG', 'Kishanpura chownk, Jalandhar', 5500, 'Wifi, AC, Cooler', 'Boys', 9876543211, 'uploaded_files\\feeling.png');

-- --------------------------------------------------------

--
-- Table structure for table `pg_enquiry`
--

CREATE TABLE `pg_enquiry` (
  `id` int(10) NOT NULL,
  `pg_id` int(10) NOT NULL,
  `username` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `message` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pg_enquiry`
--

INSERT INTO `pg_enquiry` (`id`, `pg_id`, `username`, `email`, `message`) VALUES
(1, 2, 'Gurminder', 'o7services038@gmail.com', 'bdfbsbfjsd'),
(2, 2, 'Gurminder Singh', 'singh@gmail.com', 'Just for checking enquire');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(10) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `contact` bigint(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `name`, `email`, `password`, `contact`) VALUES
(1, 'gurminder', 'gurminder@gmail.com', '123', 9876543210),
(2, 'gurminder', 'gurminder@gmail.com', '123456', 9876543210);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `pg_details`
--
ALTER TABLE `pg_details`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `pg_enquiry`
--
ALTER TABLE `pg_enquiry`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `pg_details`
--
ALTER TABLE `pg_details`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `pg_enquiry`
--
ALTER TABLE `pg_enquiry`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
