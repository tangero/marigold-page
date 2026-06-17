---
slug: "mapcon"
url: "/mobilnisite/slovnik/mapcon/"
type: "slovnik"
title: "MAPCON – Multi Access PDN Connectivity"
date: 2025-01-01
abbr: "MAPCON"
fullName: "Multi Access PDN Connectivity"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mapcon/"
summary: "Funkce 3GPP umožňující uživatelskému zařízení (UE) udržovat současná připojení k paketové datové síti (PDN) přes více 3GPP a ne-3GPP přístupových sítí (jako LTE a Wi-Fi). Umožňuje UE být připojeno ke"
---

MAPCON je funkce 3GPP umožňující uživatelskému zařízení (UE) udržovat současně více připojení k paketové datové síti (PDN) ke stejné síti, například k internetu, prostřednictvím více typů přístupu, jako jsou LTE a Wi-Fi.

## Popis

Multi Access PDN Connectivity (MAPCON) je funkce 3GPP standardizovaná ve vydání 10 a novějších, která umožňuje uživatelskému zařízení (UE) navázat a udržovat více současných připojení k paketové datové síti (PDN) ke stejnému názvu přístupového bodu ([APN](/mobilnisite/slovnik/apn/)) přes různé 3GPP a ne-3GPP rádiové přístupové sítě. Liší se od samostatných PDN připojení k různým APN; MAPCON konkrétně umožňuje připojení k jedinému APN (jako „internet“ nebo „ims“) přes více přístupů, například LTE a Wi-Fi, současně. Funkce funguje v rámci architektury Evolved Packet Core (EPC) a zahrnuje klíčové síťové prvky jako Packet Data Network Gateway (PGW), Serving Gateway (SGW) pro 3GPP přístup a evolved Packet Data Gateway (ePDG) pro nedůvěryhodný ne-3GPP přístup.

Z architektonického hlediska MAPCON spoléhá na PGW, který slouží jako společný ukotvovací bod pro PDN připojení napříč všemi přístupy. UE inicializuje PDN připojení přes primární přístup (např. LTE) ke konkrétnímu APN prostřednictvím PGW. Následně může UE navázat další PDN připojení ke stejnému APN přes sekundární přístup (např. Wi-Fi), které je ukotveno ve stejném PGW. PGW je spravuje jako samostatné kontexty přenosu (nebo PDN připojení), ale sdružuje je jako patřící stejnému UE a APN. UE je pro PDN připojení na obou přístupech přiřazena stejná IPv4 adresa a/nebo IPv6 prefix, nebo jí mohou být přiřazeny různé IP adresy v závislosti na politice operátora a konfiguraci sítě. PGW udržuje pro každý přístup samostatné tunely [GTP](/mobilnisite/slovnik/gtp/) ([GPRS](/mobilnisite/slovnik/gprs/) Tunneling Protocol) nebo vazby PMIP (Proxy Mobile IP), které se sbíhají v PGW.

Jak MAPCON funguje, zahrnuje koordinaci mezi UE a sítí. UE indikuje svou podporu MAPCON během procedur připojení nebo navazování PDN připojení. Síť ([MME](/mobilnisite/slovnik/mme/) pro 3GPP přístup, ePDG pro ne-3GPP přístup) informuje PGW, že nová žádost o PDN připojení je pro APN, ke kterému má UE již aktivní připojení na jiném přístupu. PGW pak žádosti koreluje a zřídí další kontext. Z pohledu toku provozu může mít UE IP provoz směrovaný přes kterýkoli přístup na základě politik UE, síťových politik nebo preferencí aplikace. To umožňuje případy použití, jako je přesun objemového datového provozu na Wi-Fi při zachování citlivé signalizace IMS na LTE s nízkou latencí. Funkce úzce souvisí s [ANDSF](/mobilnisite/slovnik/andsf/) (Access Network Discovery and Selection Function), která může poskytovat UE politiky pro výběr přístupu mezi těmito souběžnými připojeními.

## K čemu slouží

MAPCON byl zaveden, aby řešil rostoucí potřebu zařízení využívat více dostupných rádiových přístupových technologií současně, čímž zlepšuje uživatelský zážitek a efektivitu sítě. Před MAPCON mohlo být UE připojeno k více PDN, ale každé PDN připojení bylo vázáno na jeden typ přístupu v daném čase. Pokud UE přešlo z LTE na Wi-Fi pro dané [APN](/mobilnisite/slovnik/apn/), PDN připojení na LTE by bylo ukončeno před jeho zřízením na Wi-Fi, což způsobilo přerušení služby. Toto omezení bylo problematické, když operátoři nasazovali Wi-Fi hotspoty a chtěli je využívat k přesměrování datového provozu bez narušení probíhajících služeb.

Primární motivací bylo umožnit bezproblémové využívání přístupové sítě a směrování provozu bez přerušení relace PDN připojení. Například uživatel mohl spustit video stream přes LTE a poté vstoupit do dosahu Wi-Fi; s MAPCON by video relace mohla být bezproblémově předána na Wi-Fi (nebo dokonce využívat obě spojení současně pro agregaci) bez opětovného navázání IP relace. To je zásadní pro služby vyžadující trvalé IP adresy, jako jsou VPN nebo některé aplikace IMS. Také umožňuje operátorům implementovat inteligentní politiky řízení provozu, směrovat konkrétní toky provozu (např. best-effort internet) na Wi-Fi při zachování zásadní signalizace v 3GPP síti.

MAPCON položil základy pro pokročilejší schopnosti více přístupů v pozdějších vydáních, jako je IP Flow Mobility ([IFOM](/mobilnisite/slovnik/ifom/)) a non-seamless WLAN offload. Představoval posun od přístupově specifických PDN připojení k přístupově agnostickému PDN připojení, což je v souladu s vizí jednotné jádrové sítě (EPC), která zachází s 3GPP a ne-3GPP přístupy jako s rovnocennými. To byl klíčový krok k opravdové konvergenci sítí a schopnosti poskytovat konzistentní služby napříč heterogenními přístupovými sítěmi.

## Klíčové vlastnosti

- Umožňuje UE udržovat současná PDN připojení ke stejnému APN přes více 3GPP a ne-3GPP přístupů.
- Ukotvuje více přístupových připojení pro jediný APN ve společném PGW v EPC.
- Podporuje přiřazení stejné IP adresy (adres) UE napříč různými přístupy pro kontinuitu relace.
- Umožňuje síťové a uživatelské politiky směrování provozu napříč souběžnými připojeními.
- Vyžaduje koordinaci mezi UE, MME/ePDG a PGW během navazování PDN připojení.
- Usnadňuje bezproblémové přesměrování provozu a vyrovnávání zátěže mezi přístupovými sítěmi bez přerušení IP relací.

## Související pojmy

- [APN – Access Point Name](/mobilnisite/slovnik/apn/)
- [ANDSF – Access Network Discovery and Selection Function](/mobilnisite/slovnik/andsf/)
- [IFOM – IP Flow Mobility](/mobilnisite/slovnik/ifom/)
- [EPDG – Evolved Packet Data Gateway](/mobilnisite/slovnik/epdg/)

## Definující specifikace

- **TS 23.402** (Rel-19) — EPC for Non-3GPP Access (PMIP)
- **TS 24.302** (Rel-19) — Access to EPC via non-3GPP networks; Stage 3
- **TS 24.312** (Rel-19) — ANDSF Management Objects Specification
- **TS 32.251** (Rel-19) — PS Domain Charging Management
- **TS 37.834** (Rel-12) — WLAN/3GPP Radio Interworking Study

---

📖 **Anglický originál a plná specifikace:** [MAPCON na 3GPP Explorer](https://3gpp-explorer.com/glossary/mapcon/)
