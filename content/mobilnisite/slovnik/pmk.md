---
slug: "pmk"
url: "/mobilnisite/slovnik/pmk/"
type: "slovnik"
title: "PMK – Pairwise Master Key"
date: 2025-01-01
abbr: "PMK"
fullName: "Pairwise Master Key"
category: "Security"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pmk/"
summary: "Pairwise Master Key (PMK) je kryptografický klíč odvozený během procedur autentizace a dohody o klíči v bezdrátových sítích. Slouží jako kořenový klíč pro generování šifrovacích klíčů specifických pro"
---

PMK je kořenový kryptografický klíč odvozený během autentizace za účelem generování klíčů specifických pro relaci pro zabezpečení spojení mezi uživatelským zařízením a síťovým přístupovým bodem v bezdrátových sítích, jako jsou Wi-Fi a 3GPP-WLAN.

## Popis

Pairwise Master Key (PMK) je základní bezpečnostní klíč v rámcích autentizace a hierarchie klíčů, nejvýznamněji definovaný v [IEEE](/mobilnisite/slovnik/ieee/) 802.11i pro zabezpečení Wi-Fi a přijatý organizací 3GPP pro zabezpečení spolupráce mezi systémy 3GPP a bezdrátovými lokálními sítěmi ([WLAN](/mobilnisite/slovnik/wlan/)). PMK je 256bitový klíč, který funguje jako kořenový nebo výchozí materiál, ze kterého jsou odvozeny všechny přechodné relací klíče používané pro šifrování a ochranu integrity datového provozu. Jeho vygenerování je vyvrcholením úspěšného autentizačního procesu. V kontextu spolupráce 3GPP-WLAN (např. přístup přes důvěryhodnou WLAN založený na S2a) autentizace typicky používá rámec Extensible Authentication Protocol ([EAP](/mobilnisite/slovnik/eap/)) s metodou specifickou pro 3GPP, jako je EAP-AKA nebo EAP-AKA'. Během této EAP výměny se UE (Supplicant) autentizuje u jádrové sítě 3GPP (Authentication Server, typicky 3GPP [AAA](/mobilnisite/slovnik/aaa/) Server). Po úspěšné autentizaci odvodí jak UE, tak AAA server Master Session Key ([MSK](/mobilnisite/slovnik/msk/)) podle specifikace EAP metody. V architekturách 3GPP je tato MSK následně použita k odvození PMK. PMK je doručen ze serveru AAA k přístupovému bodu WLAN (Authenticator), který obsluhuje UE. [AP](/mobilnisite/slovnik/ap/) a UE nyní sdílejí stejný PMK. Toto sdílené tajemství je pak použito jako vstup do 4-way handshake definovaného v IEEE 802.11i. 4-way handshake je protokol vzájemné autentizace a potvrzení klíče, který dokazuje, že obě strany vlastní stejný PMK, a co je důležitější, odvozuje nové, pro relaci specifické Pairwise Transient Keys ([PTK](/mobilnisite/slovnik/ptk/)). PTK je generován oběma stranami pomocí pseudo-náhodné funkce, která jako vstup bere PMK, nonce AP (ANonce), nonce UE (SNonce) a [MAC](/mobilnisite/slovnik/mac/) adresy AP a UE. PTK je následně rozdělen na samostatné klíče pro šifrování (např. Temporal Key pro TKIP nebo CCMP) a ochranu integrity. Zabezpečení celé následné datové relace závisí na utajení a síle původního PMK. V čistě 3GPP mobilních kontextech se termín PMK také používá v rámci hierarchie klíčů pro určité funkce, jako je komunikace Vehicle-to-Everything (V2X) nebo služby založené na blízkosti (ProSe), kde může být odvozen z dlouhodobých klíčů v modulu Universal Subscriber Identity Module (USIM) pro zabezpečení přímých spojení mezi zařízeními.

## K čemu slouží

PMK existuje za účelem vytvoření silného, sdíleného tajemství mezi klientem a přístupovým bodem *po* úspěšné autentizaci, které pak může být použito k efektivnímu odvozování nových, pro relaci specifických šifrovacích klíčů. Toto oddělení úkolů je pro zabezpečení a výkon klíčové. Výpočetně náročný proces autentizace a dohody o klíči (jako je EAP-AKA) proběhne jednou a vytvoří dlouhodobě platný PMK. Lehčí 4-way handshake, využívající PMK, pak může být prováděn častěj – například pokaždé, když se zařízení přesune k novému AP nebo znovu asociuje – za účelem generování nových PTK bez opakování plné autentizace. Tím je zajištěna dokonalá dopředná utajenost pro jednotlivé relace a omezen dopad v případě kompromitace relací klíče. V historickém kontextu Wi-Fi používalo zabezpečení před standardem 802.11i (WEP) statické, ručně konfigurované klíče, které byly sdíleny mezi všemi uživateli a nikdy se neměnily, což je činilo velmi zranitelnými. Zavedení hierarchie klíčů založené na PMK se standardem 802.11i (WPA2/WPA3) bylo revolučním zlepšením. Pro 3GPP umožnilo přijetí tohoto modelu pro spolupráci s WLAN (počínaje Release 6 a vylepšené v pozdějších vydáních) mobilním operátorům bezpečně rozšířit své služby přes nedůvěryhodné Wi-Fi sítě využitím jejich robustní mobilní autentizace (založené na USIM) k vygenerování silného PMK, čímž vytvořili bezproblémový a bezpečný zážitek z 'hotspotu'. Vyřešilo to problém poskytování standardizovaného, kryptograficky silného přístupového zabezpečení pro ne-3GPP přístupové sítě.

## Klíčové vlastnosti

- 256bitový kryptografický klíč sloužící jako kořen pro odvozování relacích klíčů
- Odvozený z úspěšné EAP autentizace (např. EAP-AKA') při spolupráci 3GPP-WLAN
- Bezpečně doručený ze serveru AAA k přístupovému bodu WLAN (Authenticator)
- Použitý jako primární vstup do IEEE 802.11i 4-way handshake
- Umožňuje generování nových Pairwise Transient Keys (PTK) pro každou relaci
- Základní prvek zabezpečení pro spolupráci 3GPP-WLAN, V2X a přímou komunikaci ProSe

## Související pojmy

- [PTK – ProSe Traffic Key](/mobilnisite/slovnik/ptk/)

## Definující specifikace

- **TS 33.885** (Rel-14) — Security Study for V2X Services
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [PMK na 3GPP Explorer](https://3gpp-explorer.com/glossary/pmk/)
