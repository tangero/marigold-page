---
slug: "pn"
url: "/mobilnisite/slovnik/pn/"
type: "slovnik"
title: "PN – Personal Network"
date: 2025-01-01
abbr: "PN"
fullName: "Personal Network"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pn/"
summary: "Uživatelsky orientovaný síťový koncept, ve kterém zařízení osoby (telefony, notebooky, tablety, senzory) vytvářejí zabezpečenou, vzájemně propojenou osobní síť (personal area network). Rozšiřuje osobn"
---

PN (Personal Network) je uživatelsky orientovaný síťový koncept, ve kterém zařízení osoby vytvářejí zabezpečenou, vzájemně propojenou osobní síť (personal area network) za účelem rozšíření služeb napříč více zařízeními a přístupovými technologiemi.

## Popis

Personal Network (PN) je servisní architektura definovaná 3GPP, která vytváří uživatelsky orientovanou virtuální síť složenou ze souboru zařízení osoby, známých jako Personal Network Elements (PNEs). Mezi tato [PNE](/mobilnisite/slovnik/pne/) mohou patřit mobilní telefony, notebooky, tablety, nositelná zařízení, senzory a domácí spotřebiče. PN není fyzickou sítí, ale logickým seskupením a rámcem pro správu, který umožňuje těmto různorodým zařízením vzájemně se objevovat, bezpečně se propojovat a sdílet služby a data, jako by byla součástí jediné soudržné sítě. Architektura je založena na klíčové entitě zvané funkce Personal Network Management ([PNM](/mobilnisite/slovnik/pnm/)), která je zodpovědná za registraci PN, objevování, zabezpečení a poskytování služeb.

Provoz PN zahrnuje několik klíčových fází. Nejprve se PNE zaregistrují u PNM a deklarují své schopnosti a uživatelské preference. PNM spravuje profil PN pro uživatele. Mechanismy objevování pak umožňují PNE ve stejné PN, aby se vzájemně našla, a to i při připojení přes různé přístupové sítě (např. 3GPP mobilní síť, Wi-Fi, Bluetooth). Jádrovou součástí je PN Gateway (PN GW), který funguje jako zprostředkovatel nebo proxy, zejména pro PNE, která nejsou přímo dostupná na veřejném internetu (např. zařízení za [NAT](/mobilnisite/slovnik/nat/) v domácí síti). PN GW usnadňuje komunikaci a doručování služeb mezi PNE a mezi PN a externími sítěmi nebo poskytovateli služeb.

Základem jsou zabezpečení a ochrana soukromí. PN vytváří doménu důvěry, často využívající přihlašovací údaje z předplatného 3GPP (např. [SIM](/mobilnisite/slovnik/sim/) karta) jako kořen důvěry. Komunikace mezi PNE může být zabezpečena pomocí klíčů odvozených z tohoto vztahu důvěry. Architektura PN umožňuje řadu služeb: bezproblémový přenos relace (např. přesunutí videohovoru z telefonu na [TV](/mobilnisite/slovnik/tv/)), jednotné zasílání zpráv, sdílení osobních dat napříč zařízeními a vzdálený přístup k domácím zařízením. Abstrahuje složitost podkladové sítě a poskytuje uživateli konzistentní, personalizované služební prostředí bez ohledu na používané zařízení nebo přístupovou technologii.

## K čemu slouží

Koncept Personal Network vznikl jako odpověď na rostoucí množství osobních zařízení a uživatelskou touhu po jednotném, bezproblémovém zážitku napříč nimi. Před PN zařízení fungovala převážně izolovaně a pro sdílení a připojení byla nutná ruční konfigurace. Služby byly často vázány na jedno zařízení nebo přístupovou metodu. Architektura PN byla vytvořena, aby tento rozdrobený stav vyřešila, a poskytla standardizovaný způsob správy osobního připojení a služeb ve světě s více zařízeními a přístupy.

Její vývoj v rámci 3GPP, počínaje Release 6, byl motivován potřebou operátorů udržet relevanci a poskytovat přidané služby tváří v tvář aplikacím typu Over-The-Top ([OTT](/mobilnisite/slovnik/ott/)). Tím, že nabízeli standardizovaný, sítí podporovaný rámec pro osobní sítě, mohli operátoři využít svých klíčových aktiv – identitu účastníka, fakturační vztah a řízení sítě – k poskytování zabezpečených, spolehlivých a spravovatelných služeb osobních sítí. Řešila omezení proprietárních řešení tím, že poskytovala interoperabilní standard, umožňovala kontinuitu služeb a vytvářela platformu pro inovativní personalizované služby, které mohly být spravovány operátorem. Koncept PN položil základy pro pozdější vývoj, jako je komunikace zařízení s zařízením ([D2D](/mobilnisite/slovnik/d2d/)) a internet věcí (IoT), kde je správa skupin osobních zařízení zásadní.

## Klíčové vlastnosti

- Uživatelsky orientované logické seskupení více zařízení (Personal Network Elements)
- Centralizovaná správa prostřednictvím funkce Personal Network Management (PNM)
- Podpora vzájemného objevování zařízení a komunikace napříč heterogenními přístupovými sítěmi
- Využití PN Gateway (PN GW) k umožnění připojení pro ne-IP nebo soukromě adresovaná zařízení
- Silné zabezpečení založené na přihlašovacích údajích předplatného 3GPP a vytvoření domény důvěry PN
- Umožňuje kontinuitu služeb, sdílení osobních dat a vzdálený přístup napříč zařízeními uživatele

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.259** (Rel-19) — Personal Network Management Requirements
- **TR 22.978** (Rel-19) — Feasibility of All-IP Network (AIPN) in 3GPP
- **TR 22.980** (Rel-19) — Network Composition Feasibility Study
- **TS 23.259** (Rel-19) — Personal Network Management (PNM) Procedures
- **TS 24.259** (Rel-19) — Personal Network Management (PNM) Protocol Details
- **TS 25.223** (Rel-19) — UTRA Physical Layer TDD Spreading & Modulation
- **TS 33.812** (Rel-9) — M2M Remote Subscription Management Security
- **TR 38.808** (Rel-17) — Study on NR above 52.6 GHz to 71 GHz

---

📖 **Anglický originál a plná specifikace:** [PN na 3GPP Explorer](https://3gpp-explorer.com/glossary/pn/)
