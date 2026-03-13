-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 28/07/2025 às 14:31
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `banco007`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `carro`
--

CREATE TABLE `carro` (
  `id_carro` int(11) NOT NULL,
  `nome_carro` varchar(30) NOT NULL,
  `marca` varchar(30) NOT NULL,
  `modelo` varchar(30) NOT NULL,
  `ano` int(4) NOT NULL,
  `cor` varchar(20) NOT NULL,
  `preco` decimal(7,3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Despejando dados para a tabela `carro`
--

INSERT INTO `carro` (`id_carro`, `nome_carro`, `marca`, `modelo`, `ano`, `cor`, `preco`) VALUES
(1, 'Opala', 'Chevrolet', 'Diplomata', 1989, 'Azul', 50.000),
(2, 'Gol', 'Volkswagen', 'GTI', 1993, 'Vermelho', 60.000),
(3, 'Maverick', 'Ford', 'GT', 1974, 'Prata', 100.000),
(4, 'Fusca', 'Volkswagen', 'Beetle', 1960, 'Preto', 90.000);

-- --------------------------------------------------------

--
-- Estrutura para tabela `cliente`
--

CREATE TABLE `cliente` (
  `id_cliente` int(11) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `sobrenome` varchar(50) NOT NULL,
  `endereco` varchar(50) NOT NULL,
  `bairro` varchar(30) NOT NULL,
  `cidade` varchar(30) NOT NULL,
  `uf` char(2) NOT NULL,
  `telefone` bigint(11) NOT NULL,
  `cpf` varchar(11) NOT NULL,
  `data_nasc` date NOT NULL,
  `idade` int(3) NOT NULL,
  `sexo` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Despejando dados para a tabela `cliente`
--

INSERT INTO `cliente` (`id_cliente`, `nome`, `sobrenome`, `endereco`, `bairro`, `cidade`, `uf`, `telefone`, `cpf`, `data_nasc`, `idade`, `sexo`) VALUES
(1, 'Valdisney', 'Dysnei', 'Venâncio Aires 93', 'Azenha', 'Porto Alegre', 'RS', 222222222, '77777777777', '1990-10-23', 40, 'Masculino'),
(2, 'Patinhas', 'Pato', 'Lima e Silva 93', 'Cidade Baixa', 'Porto Algre', 'RS', 51666666666, '66666666666', '1980-12-20', 43, 'Masculino'),
(3, 'Alerquina', 'Coringa', 'Andradas 93', 'Centro', 'Porto Alegre', 'RS', 51444444444, '99999999999', '2000-11-12', 25, 'Feminino'),
(4, 'Moa', 'Capirota', 'Rua da praia', 'Casvieiras', 'Florianópolis', 'SC', 48888888888, '55555555555', '2018-11-20', 7, 'Fiminino');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `carro`
--
ALTER TABLE `carro`
  ADD PRIMARY KEY (`id_carro`);

--
-- Índices de tabela `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`id_cliente`),
  ADD UNIQUE KEY `cpf` (`cpf`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `carro`
--
ALTER TABLE `carro`
  MODIFY `id_carro` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de tabela `cliente`
--
ALTER TABLE `cliente`
  MODIFY `id_cliente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
