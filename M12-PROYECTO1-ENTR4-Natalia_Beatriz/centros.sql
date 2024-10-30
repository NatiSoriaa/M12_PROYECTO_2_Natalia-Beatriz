-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 30, 2024 at 12:48 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `centros`
--

-- --------------------------------------------------------

--
-- Table structure for table `centro_educacion`
--

CREATE TABLE `centro_educacion` (
  `id_educacion` int(11) NOT NULL,
  `nombre_educacion` varchar(255) NOT NULL,
  `fecha_inicio` date DEFAULT NULL,
  `codigo_postal_educacion` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `centro_educacion`
--

INSERT INTO `centro_educacion` (`id_educacion`, `nombre_educacion`, `fecha_inicio`, `codigo_postal_educacion`) VALUES
(1, 'Espai Familiar de Criança Municipal Socioeducatiu La Casa dels Colors', '2002-01-08', 8038),
(2, 'Facultat de Filosofia - UB', '1988-04-11', 8001),
(3, 'Col·legi d\'Educació Especial Pont del Dragó', '1989-04-18', 8027),
(4, 'Centre de Recerca en Estudi de les Dones (UB)', '1985-06-17', 8028),
(5, 'Escola Tècnica Superior d\'Enginyeria de Camins, Canals i Ports de Barcelona - UPC', '1987-10-13', 8034),
(6, 'Centre Perfeccionament Enric Mestres', '1996-09-18', 8015),
(7, 'Autoescola Carmel', '1996-09-18', 8032),
(8, 'Llar d\'Infants Tagore', '1984-05-30', 8006),
(9, 'Centre de Formació de Persones Adultes Montserrat Roig', '1990-07-27', 8018),
(10, 'Facultat de Ciències Econòmiques i Empresarials - UPF', '1990-10-18', 8005),
(11, 'Centre de Joves i Adults', '2000-01-13', 8024),
(12, 'Escola Bressol Municipal L\'Oreneta', '2002-04-03', 8017),
(13, 'Escola Bressol Municipal L\'Arquet', '2002-04-03', 8035),
(14, 'Escola Bressol Municipal El Caminet del Besòs', '2002-04-03', 8030),
(15, 'Escola Forca', '1988-03-17', 8003),
(16, 'Escola Barcelona High School', '2024-05-24', 8012),
(17, 'Espai Familiar de Criança Municipal El Galliner', '2022-09-29', 8031),
(18, 'Escola de Busseig 4all Divers', '2022-01-28', 8014),
(19, 'Escola Tècnica Superior d\'Enginyeria La Salle - URL', '2022-06-30', 8022),
(20, 'Espai Familiar de Criança Municipal Pere Calafell (en construcció)', '2023-03-03', 8020),
(21, 'Institut Lluïsa Cura', '1989-11-16', 8011),
(22, 'Escola Bressol Municipal El Vent', '1990-10-05', 8042),
(23, 'Escola Mallorquí', '2002-05-09', 8010),
(24, 'Centre Educatiu Ramón y Cajal', '1985-05-31', 8037),
(25, 'Institut Escola Ciutat Comtal', '1989-03-02', 8033),
(26, 'Centre Educatiu Claret', '1989-07-14', 8025),
(27, 'Centre educatiu Learnlife', '2024-05-27', 8007),
(28, 'Institut de Ciències Polítiques i Socials', '1989-03-06', 8008),
(29, 'Llar d\'Infants Sol Solet', '1987-11-12', 8013),
(30, 'Llar d\'Infants Petit Món de les Corts', '1987-11-17', 8029),
(31, 'Escola Estel-Guinardó', '1989-07-27', 8041),
(32, 'Institut Flos i Calcat', '1989-03-02', 8016),
(33, 'European University', '1990-01-26', 8021),
(34, 'Centre de Recursos Pedagògics de Ciutat Vella', '1992-02-07', 8002),
(35, 'Escola de Música Aula de Música 7', '1989-05-22', 8009),
(36, 'Escola Bressol Municipal Bellmunt', '1990-06-07', 8004);

-- --------------------------------------------------------

--
-- Table structure for table `centro_sanidad`
--

CREATE TABLE `centro_sanidad` (
  `id_sanidad` int(11) NOT NULL,
  `nombre_sanidad` varchar(255) NOT NULL,
  `nombre_barrio` varchar(255) DEFAULT NULL,
  `codigo_postal_sanidad` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `centro_sanidad`
--

INSERT INTO `centro_sanidad` (`id_sanidad`, `nombre_sanidad`, `nombre_barrio`, `codigo_postal_sanidad`) VALUES
(1, 'Hospital de Dia Còrsega', 'el Camp de l\'Arpa del Clot', 8026),
(2, 'Centre d\'Atenció Primària Roger', 'Sants - Badal', 8028),
(3, 'Hospital de Dia per Adolescents en Salut Mental', 'la Marina de Port', 8038),
(4, 'Centre d\'Atenció Primària El Clot', 'el Clot', 8018),
(5, 'Centre d\'Atenció Primària Vallcarca-Sant Gervasi', 'Vallcarca i els Penitents', 8023),
(6, 'Hospital  Sociosanitari Mutuam Güell', 'la Salut', 8024),
(7, 'Clínica Oftalmologica Castanera', 'Sant Gervasi - la Bonanova', 8022),
(8, 'Clínica Geriàtrica Solàrium', 'Vallcarca i els Penitents', 8035),
(9, 'Hospital de Dia d\'Adolescents Les Corts - Sarrià - Sant Gervasi', 'Sarrià', 8017),
(10, 'Centre d\'Urgències d\'Atenció Primària  Ciutat Vella - Peracamps', 'el Raval', 8001),
(11, 'Centre d\'Urgències d\'Atenció Primària Casernes de Sant Andreu', 'Sant Andreu', 8030),
(12, 'Centre Hospitalari Copèrnic', 'Sant Gervasi - Galvany', 8006),
(13, 'Centre d\'Atenció Primària Adrià', 'Sant Gervasi - Galvany', 8021),
(14, 'Clínica Institut Marquès', 'les Corts', 8034),
(15, 'Centre d\'Atenció Primària Poblenou', 'el Poblenou', 8005),
(16, 'Centre d\'Atenció Primària Numància', 'Sants', 8029),
(17, 'Hospital de la Santa Creu i Sant Pau', 'el Guinardó', 8041),
(18, 'Centre de Dia Serveis Geriàtrics de Barcelona *Av Meridiana', 'la Sagrera', 8027),
(19, 'Aprovat el projecte del nou CAP Fort Pienc  (previst obertura durant el 2025)', 'el Fort Pienc', 0),
(20, 'Hospital Clínic i Provincial', 'l\'Antiga Esquerra de l\'Eixample', 8036),
(21, 'Centre d\'Atenció Primària Chafarinas', 'la Trinitat Nova', 8033),
(22, 'Centre d\'Atenció Primària Turó', 'el Turó de la Peira', 8031),
(23, 'Centre d\'Atenció Primària El Carmel', 'el Carmel', 8032),
(24, 'Hospital de Dia', 'el Besòs i el Maresme', 8019),
(25, 'Centre d\'Atenció Primària Bordeta - Magòria', 'la Bordeta', 8014),
(26, 'Comunitat Terapèutica Clínica Llúria', 'la Dreta de l\'Eixample', 8008),
(27, 'Centre d\'Atenció Primària Barceloneta', 'la Barceloneta', 8003),
(28, 'Centre d\'Atenció Primaria', 'Vilapicina i la Torre Llobeta', 8016),
(29, 'Centre d\'Atenció Primària Pare Claret', 'el Camp d\'en Grassot i Gràcia Nova', 8037),
(30, 'Centre d\'Atenció Primària Sagrada Família', 'la Sagrada Família', 8025),
(31, 'Centre d\'Atenció Primària Guineueta', 'la Guineueta', 8042),
(32, 'Centre d\'Atenció Primària Passeig Sant Joan', 'el Fort Pienc', 8010),
(33, 'Centre d\'Atenció Primària Sant Martí', 'Sant Martí de Provençals', 8020),
(34, 'Clínica Centro Médico Aragón', 'la Nova Esquerra de l\'Eixample', 8015),
(35, 'Centre d\'Atenció Primària Les Hortes', 'el Poble-sec', 8004),
(36, 'Centre d\'Atenció Primària Gòtic', 'el Barri Gòtic', 8002),
(37, 'Centre d\'Atenció Primària Roger de Flor', 'la Dreta de l\'Eixample', 8013),
(38, 'Hospital de Nens de Barcelona', 'la Dreta de l\'Eixample', 8009);

-- --------------------------------------------------------

--
-- Table structure for table `codigo_postal_centros`
--

CREATE TABLE `codigo_postal_centros` (
  `id_educacion` int(11) NOT NULL,
  `codigo_postal_educacion` int(11) DEFAULT NULL,
  `id_sanidad` int(11) NOT NULL,
  `codigo_postal_sanidad` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `codigo_postal_centros`
--

INSERT INTO `codigo_postal_centros` (`id_educacion`, `codigo_postal_educacion`, `id_sanidad`, `codigo_postal_sanidad`) VALUES
(1, 8038, 1, 8026),
(2, 8001, 2, 8028),
(3, 8027, 3, 8038),
(4, 8028, 4, 8018),
(5, 8034, 5, 8023),
(6, 8015, 6, 8024),
(7, 8032, 7, 8022),
(8, 8006, 8, 8035),
(9, 8018, 9, 8017),
(10, 8005, 10, 8001),
(11, 8024, 11, 8030),
(12, 8017, 12, 8006),
(13, 8035, 13, 8021),
(14, 8030, 14, 8034),
(15, 8003, 15, 8005),
(16, 8012, 16, 8029),
(17, 8031, 17, 8041),
(18, 8014, 18, 8027),
(19, 8022, 19, 0),
(20, 8020, 20, 8036),
(21, 8011, 21, 8033),
(22, 8042, 22, 8031),
(23, 8010, 23, 8032),
(24, 8037, 24, 8019),
(25, 8033, 25, 8014),
(26, 8025, 26, 8008),
(27, 8007, 27, 8003),
(28, 8008, 28, 8016),
(29, 8013, 29, 8037),
(30, 8029, 30, 8025),
(31, 8041, 31, 8042),
(32, 8016, 32, 8010),
(33, 8021, 33, 8020),
(34, 8002, 34, 8015),
(35, 8009, 35, 8004),
(36, 8004, 36, 8002);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `centro_educacion`
--
ALTER TABLE `centro_educacion`
  ADD PRIMARY KEY (`id_educacion`),
  ADD UNIQUE KEY `unique_codigo_postal_educacion` (`codigo_postal_educacion`);

--
-- Indexes for table `centro_sanidad`
--
ALTER TABLE `centro_sanidad`
  ADD PRIMARY KEY (`id_sanidad`),
  ADD UNIQUE KEY `unique_codigo_postal_sanidad` (`codigo_postal_sanidad`);

--
-- Indexes for table `codigo_postal_centros`
--
ALTER TABLE `codigo_postal_centros`
  ADD PRIMARY KEY (`id_educacion`,`id_sanidad`),
  ADD KEY `id_sanidad` (`id_sanidad`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `centro_educacion`
--
ALTER TABLE `centro_educacion`
  MODIFY `id_educacion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;

--
-- AUTO_INCREMENT for table `centro_sanidad`
--
ALTER TABLE `centro_sanidad`
  MODIFY `id_sanidad` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=40;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `codigo_postal_centros`
--
ALTER TABLE `codigo_postal_centros`
  ADD CONSTRAINT `codigo_postal_centros_ibfk_1` FOREIGN KEY (`id_educacion`) REFERENCES `centro_educacion` (`id_educacion`),
  ADD CONSTRAINT `codigo_postal_centros_ibfk_2` FOREIGN KEY (`id_sanidad`) REFERENCES `centro_sanidad` (`id_sanidad`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
