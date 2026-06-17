---
slug: "gnp"
url: "/mobilnisite/slovnik/gnp/"
type: "slovnik"
title: "GNP – Generic Network Product Class"
date: 2026-01-01
abbr: "GNP"
fullName: "Generic Network Product Class"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/gnp/"
summary: "Generic Network Product Class (GNP) je koncept zabezpečení a záruk, který definuje kategorii síťových produktů implementujících společnou sadu funkcí definovaných 3GPP. Umožňuje standardizované bezpeč"
---

GNP je koncept zabezpečení a záruk, který definuje kategorii síťových produktů implementujících společnou sadu funkcí definovaných 3GPP, aby umožnil standardizované bezpečnostní hodnocení a certifikaci.

## Popis

Generic Network Product Class (GNP) je rámec definovaný v bezpečnostních specifikacích 3GPP, zejména v TS 33.926, pro kategorizaci síťových produktů na základě jejich implementovaných 3GPP funkcí za účelem bezpečnostního hodnocení a zajištění. GNP představuje třídu síťových produktů – jako jsou konkrétní typy Mobility Management Entities ([MME](/mobilnisite/slovnik/mme/)), Serving Gateways (S-GW) nebo Access and Mobility Management Functions ([AMF](/mobilnisite/slovnik/amf/)) – které všechny poskytují stejnou standardizovanou sadu schopností definovaných 3GPP. Hlavní myšlenkou je, že bezpečnostní požadavky, testovací případy a metodiky hodnocení lze definovat na úrovni třídy, nikoli pro každý jednotlivý produkt, což zefektivňuje certifikační proces a zajišťuje konzistentní bezpečnostní základ napříč odvětvím.

Z architektonického hlediska je koncept GNP součástí metodiky 3GPP Security Assurance Specification (SCAS). Funguje tak, že nejprve definuje obecnou třídu síťového produktu na základě technických specifikací 3GPP pro danou síťovou funkci. Pro každý GNP je odvozena podrobná sada bezpečnostních požadavků z bezpečnostních specifikací 3GPP (řada TS 33.) a širších osvědčených postupů zabezpečení. Tyto požadavky pokrývají oblasti jako autentizace, důvěrnost dat, integrita, dostupnost a bezpečné protokolování. Dodavatelé vyvíjející produkt spadající pod konkrétní GNP musí navrhnout a implementovat svůj produkt tak, aby splňoval tyto požadavky na úrovni třídy. Produkt je následně podroben hodnocení vůči standardizované Security Assurance Specification (SCAS) pro daný GNP.

Proces zahrnuje několik klíčových komponent: samotnou definici GNP, přidružený dokument SCAS podrobně popisující bezpečnostní požadavky a testovací případy a metodiku hodnocení prováděnou akreditovanými laboratořemi. Například GNP pro 5G Core Access and Mobility Management Function (AMF) by uváděl všechny povinné a volitelné 3GPP funkce, které musí AMF podporovat. Odpovídající SCAS by specifikoval, jak testovat implementaci bezpečnostních protokolů AMF, jako je [NAS](/mobilnisite/slovnik/nas/) security, jeho odolnost vůči útokům typu denial-of-service a jeho zabezpečená rozhraní pro správu. Tento strukturovaný přístup zajišťuje, že bez ohledu na dodavatele jakákoli AMF certifikovaná pod tímto GNP splňuje stejné přísné bezpečnostní standardy.

Role GNP v síti je zásadní pro budování důvěry ve více-dodavatelské, interoperabilní systémy 3GPP. Tím, že poskytuje jasný, standardizovaný cíl pro bezpečnostní hodnocení, snižuje nejednoznačnost pro dodavatele, operátory a regulátory. Síťoví operátoři pořizující zařízení mohou odkazovat na certifikaci GNP jako na důkaz souladu se zabezpečením, čímž zjednodušují své vlastní posuzování rizik. Dále usnadňuje globální přijetí na trhu tím, že sladí bezpečnostní hodnocení napříč různými národními certifikačními schématy (jako jsou ta založená na Common Criteria). Rámec GNP, vyvíjející se od Rel-13, je klíčovým prvkem pro zabezpečení složitých 5G sítí, zejména v oblastech, jako je síťové dělení (network slicing) a edge computing, kde musí být bezpečnostní hranice a odpovědnosti jasně definovány a zajištěny.

## K čemu slouží

Rámec Generic Network Product Class (GNP) byl vytvořen, aby řešil kritickou výzvu zajištění konzistentního a ověřitelného zabezpečení napříč více-dodavatelskými nasazeními sítí 3GPP. Před jeho zavedením byla bezpečnostní hodnocení síťových produktů často ad-hoc, specifická pro dodavatele nebo založená na obecných standardech [IT](/mobilnisite/slovnik/it/) zabezpečení, které plně nezachycovaly jedinečné hrozby a požadavky telekomunikačních sítí. To vedlo k potenciálním bezpečnostním mezerám, zvýšeným nákladům pro operátory provádějící individuální posouzení a překážkám pro vstup na trh pro dodavatele čelící různorodým národním certifikačním požadavkům.

Motivace pro GNP vznikla s rostoucí složitostí a softwarově definovanou povahou síťových funkcí, zejména jak se sítě vyvíjely směrem k 5G a cloud-nativním architekturám. Tradiční přístup testování fyzických „black boxů“ byl nedostatečný pro virtualizované síťové funkce (VNF) a cloud-nativní síťové funkce ([CNF](/mobilnisite/slovnik/cnf/)). 3GPP ve spolupráci s normalizačními orgány, jako je [GSMA](/mobilnisite/slovnik/gsma/), a regulačními skupinami vyvinulo pracovní položku Security Assurance Specification (SCAS), jejímž základním kamenem je GNP. Řeší tento problém definováním zabezpečení na úrovni *funkčnosti* produktu (dle specifikací 3GPP), nikoli jeho *implementace*, což umožňuje standardizovaný, ale flexibilní proces zajištění.

GNP dále řeší potřebu škálovatelného zabezpečení v ekosystému s mnoha dodavateli a rychlými inovačními cykly. Stanovením společných bezpečnostních požadavků pro třídu produktů (např. všechny 5G User Plane Functions) zajišťuje, že základní úroveň ochrany je vestavěna do struktury sítě. To je obzvláště důležité pro síťové dělení (network slicing), kde instance slicu může záviset na produktech od různých dodavatelů; certifikace GNP poskytuje důvěru v zabezpečení každé komponenty. V podstatě rámec GNP transformuje síťové zabezpečení z neprůhledného problému řešeného až po nasazení na transparentní požadavek ve fázi návrhu, který podporuje důvěru, interoperabilitu a rychlejší a bezpečnější inovace v ekosystému 3GPP.

## Klíčové vlastnosti

- Definuje třídu síťových produktů na základě společných funkcí definovaných 3GPP
- Slouží jako základ pro standardizované Security Assurance Specifications (SCAS)
- Umožňuje konzistentní bezpečnostní hodnocení a certifikaci napříč různými dodavateli
- Pokrývá bezpečnostní požadavky na autentizaci, důvěrnost, integritu a dostupnost
- Podporuje bezpečnostní potřeby virtualizovaných a cloud-nativních síťových funkcí (VNF/CNF)
- Usnadňuje regulatorní shodu a přijetí na trhu pro síťová zařízení

## Definující specifikace

- **TR 33.926** (Rel-20) — Security Assurance Specification (SCAS)

---

📖 **Anglický originál a plná specifikace:** [GNP na 3GPP Explorer](https://3gpp-explorer.com/glossary/gnp/)
