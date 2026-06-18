---
slug: "pei-rnti"
url: "/mobilnisite/slovnik/pei-rnti/"
type: "slovnik"
title: "PEI-RNTI – Paging Early Indication Radio Network Temporary Identifier"
date: 2025-01-01
abbr: "PEI-RNTI"
fullName: "Paging Early Indication Radio Network Temporary Identifier"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pei-rnti/"
summary: "Jedinečný identifikátor používaný ke skramblování řídicích informací v downlinku (Downlink Control Information, DCI), které nesou signál předčasné indikace stránkování (Paging Early Indication). Umožň"
---

PEI-RNTI je jedinečný identifikátor používaný ke skramblování řídicích informací v downlinku (Downlink Control Information), které nesou signál předčasné indikace stránkování (Paging Early Indication). Umožňuje skupině UE efektivně zjistit, zda musí monitorovat nadcházející příležitost pro stránkování.

## Popis

Paging Early Indication [RNTI](/mobilnisite/slovnik/rnti/) (PEI-RNTI) je dočasný identifikátor rádiové sítě (Radio Network Temporary Identifier) ve fyzické vrstvě 5G NR, speciálně navržený pro funkci předčasné indikace stránkování (Paging Early Indication, [PEI](/mobilnisite/slovnik/pei/)). RNTI je v podstatě číslo používané ke skramblování a identifikaci zpráv řídicího kanálu určených pro konkrétní UE nebo skupinu UE. PEI-RNTI je skupinový identifikátor, což znamená, že jednu hodnotu PEI-RNTI sdílí nakonfigurovaná sada UE monitorující stejnou příležitost pro předčasnou indikaci stránkování ([PEI-O](/mobilnisite/slovnik/pei-o/)). gNB používá tento PEI-RNTI ke skramblování bitů kontrolního součtu cyklickou redundancí (Cyclic Redundancy Check, [CRC](/mobilnisite/slovnik/crc/)) formátu řídicích informací v downlinku (Downlink Control Information, [DCI](/mobilnisite/slovnik/dci/)), který přenáší PEI signál.

Operačně, když gNB potřebuje upozornit skupinu UE, že budou následovat stránkovací zprávy, vygeneruje DCI na [PDCCH](/mobilnisite/slovnik/pdcch/) během PEI-O. Toto DCI je skramblováno pomocí PEI-RNTI známého cílové skupině UE. Každá UE v této skupině se při probuzení ve svém PEI-O pokusí slepě dekódovat kandidáty PDCCH pomocí svého přiřazeného PEI-RNTI. Proces je vysoce efektivní: UE potřebuje pouze provést kontrolu CRC pomocí PEI-RNTI. Pokud kontrola CRC projde, DCI je úspěšně dekódováno a jeho obsah (jednoduchý indikátor) informuje UE, aby monitorovala následující příležitost pro stránkování (Paging Occasion). Pokud není detekováno žádné DCI se shodným PEI-RNTI, UE to interpretuje jako 'negativní' PEI a vrátí se do spánkového režimu.

PEI-RNTI je klíčovou komponentou, která umožňuje skupinové adresování potřebné pro efektivní signalizaci PEI. Bez takového sdíleného identifikátoru by síť musela signalizovat každé UE individuálně, čímž by se ztratily výhody úspory energie. Hodnota PEI-RNTI je odvozena od parametrů poskytnutých UE během konfigurace, například prostřednictvím systémového informačního bloku (System Information Block, [SIB](/mobilnisite/slovnik/sib/)) nebo vyhrazené signalizace [RRC](/mobilnisite/slovnik/rrc/). Jeho použití je omezeno na fyzickou a MAC vrstvu pro specifický účel detekce PEI. Tento mechanismus je příkladem vrstveného přístupu k úspoře energie v 5G, kde minimální signál na fyzické vrstvě, efektivně adresovaný pomocí skupinového RNTI, řídí energeticky náročnější proceduru stránkování na vyšších vrstvách.

## K čemu slouží

PEI-RNTI byl vytvořen k řešení problému efektivního a spolehlivého adresování více UE pomocí jediného probouzejícího signálu s nízkou režií v rámci architektury předčasné indikace stránkování (Paging Early Indication). Před touto funkcí bylo stránkování adresováno pomocí P-RNTI, které upozornilo všechna UE v příležitosti pro stránkování, aby dekódovala následnou stránkovací zprávu, ale neposkytovalo předběžný krok filtrování s nízkou spotřebou. Potřeba vyhrazeného identifikátoru vyplynula z konstrukčního cíle PEI: být signálem s ultranízkou spotřebou, který může UE detekovat s minimálním zpracováním.

Použití sdíleného skupinového RNTI je v celulárních systémech osvědčenou a efektivní metodou pro multicastovou signalizaci řízení. PEI-RNTI toto umožňuje pro PEI, což dovoluje, aby jedna kompaktní zpráva DCI obsloužila celou skupinu UE současně. Tento návrh minimalizuje režii řídicího kanálu a složitost zpracování na straně UE ve srovnání s individuální signalizací. Byl motivován přísnými cíli pro spotřebu energie v 5G, zejména pro IoT. PEI-RNTI poskytuje nezbytný adresovací mechanismus, který činí dvoukrokový proces stránkování (kontrola PEI následovaná potenciálním dekódováním PO) proveditelným a energeticky efektivním, což přímo přispívá k prodloužení životnosti baterie zařízení, která jsou stránkována nepravidelně.

## Klíčové vlastnosti

- Skupinový dočasný identifikátor rádiové sítě (Radio Network Temporary Identifier) pro signalizaci PEI
- Používá se ke skramblování CRC DCI nesoucího předčasnou indikaci stránkování (Paging Early Indication)
- Umožňuje efektivní slepé dekódování PEI skupinou UE
- Hodnota je odvozena z konfiguračních parametrů UE (např. ze SIB nebo RRC)
- Základní prvek pro fungování funkce PEI na fyzické vrstvě
- Snižuje režii řídicího kanálu ve srovnání s individuální signalizací pro každé UE

## Související pojmy

- [RNTI – Radio Network Temporary Identifier](/mobilnisite/slovnik/rnti/)
- [P-RNTI – Paging Radio Network Temporary Identifier](/mobilnisite/slovnik/p-rnti/)

## Definující specifikace

- **TS 38.321** (Rel-19) — NR MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [PEI-RNTI na 3GPP Explorer](https://3gpp-explorer.com/glossary/pei-rnti/)
