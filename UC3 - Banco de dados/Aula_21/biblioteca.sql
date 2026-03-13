-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 29/07/2025 às 16:54
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
-- Banco de dados: `biblioteca`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `aluno`
--

CREATE TABLE `aluno` (
  `id_matricula` int(11) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `fone` varchar(11) NOT NULL,
  `endereco` varchar(100) NOT NULL,
  `sexo` char(1) NOT NULL,
  `cpf` varchar(11) NOT NULL,
  `email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Despejando dados para a tabela `aluno`
--

INSERT INTO `aluno` (`id_matricula`, `nome`, `fone`, `endereco`, `sexo`, `cpf`, `email`) VALUES
(1, 'Maria', '54666666666', 'Venâncio Aires 93', 'F', '66666666666', 'maria@gmail.com'),
(2, 'João', '51555555555', 'Lima e Silva 100', 'M', '55555555555', 'joao@gmail.com'),
(3, 'Carlos', '51444444444', 'Andradas 1000', 'M', '44444444444', 'carlos@gmail.com'),
(4, 'Clotilde', '51333333333', 'Silva Só 300', 'F', '33333333333', 'clotilde@gmail.com');

-- --------------------------------------------------------

--
-- Estrutura para tabela `autor`
--

CREATE TABLE `autor` (
  `id_autor` int(11) NOT NULL,
  `nome_completo` varchar(50) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `sobrenome` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Despejando dados para a tabela `autor`
--

INSERT INTO `autor` (`id_autor`, `nome_completo`, `nome`, `sobrenome`) VALUES
(1, 'Carlos Alberto Heuser', 'Carlos Alberto', 'HEUSER'),
(2, 'Idalberto Chiavenato', 'Idauberto', 'CHIAVENATO'),
(3, 'Paul Deitel', 'Paul', 'DEITEL');

-- --------------------------------------------------------

--
-- Estrutura para tabela `editora`
--

CREATE TABLE `editora` (
  `id_editora` int(11) NOT NULL,
  `nome` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Despejando dados para a tabela `editora`
--

INSERT INTO `editora` (`id_editora`, `nome`) VALUES
(1, 'Pearson'),
(2, 'Editora Campos'),
(3, 'Novatec');

-- --------------------------------------------------------

--
-- Estrutura para tabela `emprestimo`
--

CREATE TABLE `emprestimo` (
  `id_emprestimo` int(11) NOT NULL,
  `codigo_matricula` int(11) NOT NULL,
  `codigo_livro` int(11) NOT NULL,
  `data_retirada` date NOT NULL,
  `data_entrega` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Despejando dados para a tabela `emprestimo`
--

INSERT INTO `emprestimo` (`id_emprestimo`, `codigo_matricula`, `codigo_livro`, `data_retirada`, `data_entrega`) VALUES
(1, 1, 1, '2025-07-29', '2025-08-05'),
(2, 2, 2, '2025-07-29', '2025-08-06'),
(3, 3, 3, '2025-07-29', '2025-08-07'),
(4, 1, 1, '2025-07-29', '2025-08-05'),
(5, 2, 2, '2025-07-29', '2025-08-06'),
(6, 3, 3, '2025-07-29', '2025-08-07');

-- --------------------------------------------------------

--
-- Estrutura para tabela `genero`
--

CREATE TABLE `genero` (
  `id_genero` int(11) NOT NULL,
  `nome` varchar(30) NOT NULL,
  `sigla` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Despejando dados para a tabela `genero`
--

INSERT INTO `genero` (`id_genero`, `nome`, `sigla`) VALUES
(1, 'Informática', 'INF'),
(2, 'Administração', 'ADM'),
(3, 'Direito', 'DIR'),
(4, 'Matemática', 'MAT'),
(5, 'Esportes', 'ESP');

-- --------------------------------------------------------

--
-- Estrutura para tabela `livro`
--

CREATE TABLE `livro` (
  `id_livro` int(11) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `ano` int(4) NOT NULL,
  `edicao` int(2) NOT NULL,
  `codigo_autor` int(11) NOT NULL,
  `codigo_genero` int(11) NOT NULL,
  `codigo_editora` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Despejando dados para a tabela `livro`
--

INSERT INTO `livro` (`id_livro`, `nome`, `ano`, `edicao`, `codigo_autor`, `codigo_genero`, `codigo_editora`) VALUES
(1, 'Projeto de Banco de dados', 2020, 1, 1, 1, 1),
(2, 'Java', 2021, 3, 3, 1, 1),
(3, 'Teoria geral da Administração', 2019, 3, 2, 2, 2);

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `aluno`
--
ALTER TABLE `aluno`
  ADD PRIMARY KEY (`id_matricula`);

--
-- Índices de tabela `autor`
--
ALTER TABLE `autor`
  ADD PRIMARY KEY (`id_autor`);

--
-- Índices de tabela `editora`
--
ALTER TABLE `editora`
  ADD PRIMARY KEY (`id_editora`);

--
-- Índices de tabela `emprestimo`
--
ALTER TABLE `emprestimo`
  ADD PRIMARY KEY (`id_emprestimo`),
  ADD KEY `codigo_matricula` (`codigo_matricula`),
  ADD KEY `codigo_livro` (`codigo_livro`);

--
-- Índices de tabela `genero`
--
ALTER TABLE `genero`
  ADD PRIMARY KEY (`id_genero`);

--
-- Índices de tabela `livro`
--
ALTER TABLE `livro`
  ADD PRIMARY KEY (`id_livro`),
  ADD KEY `codigo_autor` (`codigo_autor`),
  ADD KEY `codigo_genero` (`codigo_genero`),
  ADD KEY `codigo_editora` (`codigo_editora`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `aluno`
--
ALTER TABLE `aluno`
  MODIFY `id_matricula` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de tabela `autor`
--
ALTER TABLE `autor`
  MODIFY `id_autor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de tabela `editora`
--
ALTER TABLE `editora`
  MODIFY `id_editora` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de tabela `emprestimo`
--
ALTER TABLE `emprestimo`
  MODIFY `id_emprestimo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de tabela `genero`
--
ALTER TABLE `genero`
  MODIFY `id_genero` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de tabela `livro`
--
ALTER TABLE `livro`
  MODIFY `id_livro` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `emprestimo`
--
ALTER TABLE `emprestimo`
  ADD CONSTRAINT `emprestimo_ibfk_1` FOREIGN KEY (`codigo_matricula`) REFERENCES `aluno` (`id_matricula`),
  ADD CONSTRAINT `emprestimo_ibfk_2` FOREIGN KEY (`codigo_livro`) REFERENCES `livro` (`id_livro`);

--
-- Restrições para tabelas `livro`
--
ALTER TABLE `livro`
  ADD CONSTRAINT `livro_ibfk_1` FOREIGN KEY (`codigo_autor`) REFERENCES `autor` (`id_autor`),
  ADD CONSTRAINT `livro_ibfk_2` FOREIGN KEY (`codigo_genero`) REFERENCES `genero` (`id_genero`),
  ADD CONSTRAINT `livro_ibfk_3` FOREIGN KEY (`codigo_editora`) REFERENCES `editora` (`id_editora`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
