-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 12, 2024 at 11:49 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `projet_python`
--

-- --------------------------------------------------------

--
-- Table structure for table `access`
--

CREATE TABLE `access` (
  `id_user` int(11) NOT NULL,
  `nom_user` varchar(11) NOT NULL,
  `mot_de_passe` varchar(20) NOT NULL,
  `privilege` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `access`
--

INSERT INTO `access` (`id_user`, `nom_user`, `mot_de_passe`, `privilege`) VALUES
(1, 'firas', '123', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `archive_cmd`
--

CREATE TABLE `archive_cmd` (
  `id_supp_cmd` varchar(100) NOT NULL,
  `date_supp` date NOT NULL,
  `chemin` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `archive_cmd`
--

INSERT INTO `archive_cmd` (`id_supp_cmd`, `date_supp`, `chemin`) VALUES
('0', '2024-01-10', 'D:\\Documents\\Iteam-University\\2eme\\python\\projet\\COM_firas dehech_2024-01-10_19-30-49.pdf'),
('COM_client_X_2024-01-10_23-49-18.pdf', '2024-01-10', 'D:\\Documents\\Iteam-University\\2eme\\python\\projet\\COM_client_X_2024-01-10_23-49-18.pdf'),
('COM_firas_dehech_2024-01-10_19-31-32.pdf', '2024-01-11', 'D:\\Documents\\Iteam-University\\2eme\\python\\projet\\COM_firas_dehech_2024-01-10_19-31-32.pdf');

-- --------------------------------------------------------

--
-- Table structure for table `archive_fact`
--

CREATE TABLE `archive_fact` (
  `id_supp_fac` varchar(100) NOT NULL,
  `date_supp` date NOT NULL,
  `chemin` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `archive_fact`
--

INSERT INTO `archive_fact` (`id_supp_fac`, `date_supp`, `chemin`) VALUES
('0', '2024-01-10', 'D:\\Documents\\Iteam-University\\2eme\\python\\projet\\f'),
('Fact_clt_2024-01-10_18-47-56.pdf', '2024-01-10', 'D:\\Documents\\Iteam-University\\2eme\\python\\projet\\Fact_clt_2024-01-10_18-47-56.pdf'),
('Fact_clt_2024-01-10_19-14-03.pdf', '2024-01-10', 'D:\\Documents\\Iteam-University\\2eme\\python\\projet\\Fact_clt_2024-01-10_19-14-03.pdf');

-- --------------------------------------------------------

--
-- Table structure for table `client`
--

CREATE TABLE `client` (
  `id_client` int(11) NOT NULL,
  `nom_client` varchar(20) NOT NULL,
  `adresse` varchar(20) NOT NULL,
  `adresse_email` varchar(20) NOT NULL,
  `num_tel` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `client`
--

INSERT INTO `client` (`id_client`, `nom_client`, `adresse`, `adresse_email`, `num_tel`) VALUES
(1, 'client', 'bizerte', 'client1@clt.com', 0);

-- --------------------------------------------------------

--
-- Table structure for table `commande`
--

CREATE TABLE `commande` (
  `id_cmd` varchar(50) NOT NULL,
  `chemin` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `commande`
--

INSERT INTO `commande` (`id_cmd`, `chemin`) VALUES
('COM_client_passager_2024-01-11_11-05-23.pdf', 'D:\\Documents\\Iteam-University\\2eme\\python\\projet\\COM_client_passager_2024-01-11_11-05-23.pdf');

-- --------------------------------------------------------

--
-- Table structure for table `facture`
--

CREATE TABLE `facture` (
  `id_facture` varchar(50) NOT NULL,
  `chemin` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `facture`
--

INSERT INTO `facture` (`id_facture`, `chemin`) VALUES
('Fact_client1_2024-01-10_23-01-21.pdf', 'D:\\Documents\\Iteam-University\\2eme\\python\\projet\\Fact_client1_2024-01-10_23-01-21.pdf');

-- --------------------------------------------------------

--
-- Table structure for table `produit`
--

CREATE TABLE `produit` (
  `id_produit` int(11) NOT NULL,
  `nom_produit` varchar(50) NOT NULL,
  `description` varchar(70) NOT NULL,
  `quantite` int(11) NOT NULL,
  `prix_achat` float NOT NULL,
  `prix_vente` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `produit`
--

INSERT INTO `produit` (`id_produit`, `nom_produit`, `description`, `quantite`, `prix_achat`, `prix_vente`) VALUES
(1, 'prod1', 'ce produit est un test', 81, 12.5, 18),
(2, 'prod2', 'test', 2, 9.5, 13.2),
(8, 'firas', 'description', 2, 56, 88);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `access`
--
ALTER TABLE `access`
  ADD PRIMARY KEY (`id_user`);

--
-- Indexes for table `archive_cmd`
--
ALTER TABLE `archive_cmd`
  ADD PRIMARY KEY (`id_supp_cmd`);

--
-- Indexes for table `archive_fact`
--
ALTER TABLE `archive_fact`
  ADD PRIMARY KEY (`id_supp_fac`);

--
-- Indexes for table `client`
--
ALTER TABLE `client`
  ADD PRIMARY KEY (`id_client`);

--
-- Indexes for table `commande`
--
ALTER TABLE `commande`
  ADD PRIMARY KEY (`id_cmd`);

--
-- Indexes for table `facture`
--
ALTER TABLE `facture`
  ADD PRIMARY KEY (`id_facture`);

--
-- Indexes for table `produit`
--
ALTER TABLE `produit`
  ADD PRIMARY KEY (`id_produit`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
