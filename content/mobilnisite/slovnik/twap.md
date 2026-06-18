---
slug: "twap"
url: "/mobilnisite/slovnik/twap/"
type: "slovnik"
title: "TWAP – Trusted WLAN AAA Proxy"
date: 2026-01-01
abbr: "TWAP"
fullName: "Trusted WLAN AAA Proxy"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/twap/"
summary: "Trusted WLAN AAA Proxy (TWAP) je funkce řídicí roviny v rámci důvěryhodné WLAN přístupové sítě (TWAN). Proxyuje signalizaci AAA mezi WLAN a infrastrukturou AAA 3GPP, čímž usnadňuje autentizaci, autori"
---

TWAP je funkce řídicí roviny v rámci důvěryhodné WLAN přístupové sítě, která proxyuje signalizaci AAA mezi WLAN a jádrem 3GPP, aby umožnila autentizaci uživatelských zařízení (UE) založenou na SIM kartě.

## Popis

Trusted [WLAN](/mobilnisite/slovnik/wlan/) [AAA](/mobilnisite/slovnik/aaa/) Proxy (TWAP) je klíčová funkce řídicí roviny v architektuře důvěryhodné WLAN přístupové sítě ([TWAN](/mobilnisite/slovnik/twan/)). Jejím primárním úkolem je zprostředkovávat signalizaci pro autentizaci, autorizaci a účtování (AAA) mezi uživatelským zařízením (UE) přistupujícím přes WLAN a serverem (nebo proxy) AAA 3GPP v jádrové síti mobilního operátora. TWAP sama nerozhoduje o autentizaci, ale spolehlivě přeposílá a případně překládá AAA protokoly, čímž zajišťuje efektivní komunikaci mezi WLAN přístupovým bodem a jádrem 3GPP pro správu účastníků. Je klíčovým prvkem pro zabezpečený přístup k důvěryhodným WLAN sítím založený na [SIM](/mobilnisite/slovnik/sim/) kartě.

Provozně se TWAP nachází na referenčním bodě STa, který spojuje TWAN se serverem AAA 3GPP. Když se uživatelské zařízení (UE) pokouší připojit k důvěryhodné WLAN, zahájí proceduru [EAP](/mobilnisite/slovnik/eap/) (Extensible Authentication Protocol). WLAN přístupový bod ([AP](/mobilnisite/slovnik/ap/)) přepošle EAP zprávy k TWAP pomocí protokolů jako [RADIUS](/mobilnisite/slovnik/radius/) nebo Diameter. TWAP pak funguje jako proxy a přeposílá tyto zprávy přes rozhraní STa k serveru AAA 3GPP pomocí protokolu Diameter. Server AAA komunikuje s domácím účastnickým serverem ([HSS](/mobilnisite/slovnik/hss/)), aby ověřil přihlašovací údaje uživatelského zařízení (pomocí EAP-AKA nebo EAP-AKA'). TWAP zajišťuje úspěšné dokončení celého autentizačního dialogu. Kromě počáteční autentizace se TWAP také podílí na autorizaci tím, že přenáší informace o profilu autorizovaného uživatele a případných přístupových omezeních z jádrové sítě do WLAN.

Působnost TWAP zasahuje i do správy relací a řízení politik. Po úspěšné autentizaci poskytne server AAA 3GPP TWAP informace o předplatitelském profilu a může spustit vytvoření relace uživatelské roviny. TWAP komunikuje s Trusted WLAN Access Gateway (TWAG) ve stejné TWAN, aby ho informoval o úspěšné autentizaci a poskytl potřebné parametry pro nastavení datového přenosu přes S2a. Navíc, v některých architekturách může TWAP komunikovat s funkcí Policy and Charging Rules Function (PCRF) přes referenční body Gxa/Gxb (nebo fungovat jako proxy pro takovou signalizaci), aby získal pravidla pro politiky a účtování pro účastníkovu relaci. Tato pravidla jsou pak vynucována na TWAG pro provoz v uživatelské rovině.

Stručně řečeno, TWAP je nervovým centrem řídicí roviny pro přístup přes důvěryhodnou WLAN. Abstrahuje specifika AAA protokolu WLAN od jádra 3GPP a poskytuje standardizované rozhraní založené na Diameteru. Zpracováním složité signalizace pro autentizaci a politiky umožňuje, aby byla WLAN považována za důvěryhodnou přístupovou síť 3GPP, což zajišťuje, že přístup získají pouze autorizovaní účastníci a že jejich relace jsou spravovány podle jejich profilů mobilních služeb. Tato funkce byla zásadní pro komerční nasazení bezproblémových a bezpečných služeb Wi-Fi poskytovaných operátorem.

## K čemu slouží

TWAP byl zaveden, aby vyřešil kritický problém signalizační interoperability při integraci WLAN s jádrovou sítí 3GPP. Infrastruktura WLAN tradičně používá pro řízení síťového přístupu AAA protokoly jako RADIUS, zatímco jádrová síť 3GPP používá pro svou interní AAA signalizaci protokol Diameter. TWAP byl vytvořen, aby překlenul tuto protokolovou propast, a funguje jako překladový bod nebo proxy, který umožňuje komunikaci mezi těmito dvěma odlišnými technologickými doménami. Bez něj by nebylo možné provádět autentizaci založenou na SIM kartě a řízení politik 3GPP přes důvěryhodnou WLAN.

Jeho vytvoření ve vydání 11 bylo motivováno potřebou standardizované funkce pro zpracování signalizace řídicí roviny pro nově definovanou Trusted WLAN Access Network (TWAN). Předchozí neintegrovaný přístup přes Wi-Fi vyžadoval samostatné, často webové, přihlašovací portály a přihlašovací údaje. Cílem bylo využít vysokou bezpečnost karty USIM pro přístup přes WLAN. TWAP to umožnil spolehlivým přenosem EAP autentizačních dialogů (EAP-AKA/AKA') mezi uživatelským zařízením v WLAN a serverem AAA 3GPP/HSS v jádru. Tím vyřešil problém, jak může WLAN přístupový bod, který komunikuje pomocí RADIUS/EAP, autentizovat uživatele vůči HSS 3GPP.

Kromě základní autentizace TWAP také řešil potřebu integrovaného řízení relací a politik. Umožnil přenos informací o předplatitelském profilu z jádra do přístupové sítě a usnadnil interakci s PCRF. To mobilním operátorům umožnilo aplikovat stejná sofistikovaná pravidla pro politiky a účtování na Wi-Fi provoz jako na provoz LTE, což umožnilo diferenciaci služeb, garantovanou kvalitu služeb pro služby jako VoWiFi a přesné účtování. TWAP byl tedy základní komponentou, která proměnila Wi-Fi z pouhého internetového kanálu ve spravované, zúčtovatelné a na služby citlivé rozšíření mobilní sítě.

## Klíčové vlastnosti

- Proxyuje AAA signalizaci (např. RADIUS/Diameter) mezi WLAN a serverem AAA 3GPP přes rozhraní STa
- Umožňuje autentizaci EAP-AKA/AKA', čímž zprostředkovává přístup k důvěryhodné WLAN založený na SIM kartě
- Přeposílá data o předplatitelském profilu a autorizační údaje z jádrové sítě do TWAN
- Komunikuje s TWAG, aby po úspěšné autentizaci spustil vytvoření relace uživatelské roviny
- Může fungovat jako proxy pro signalizaci Policy and Charging Control (PCC) mezi TWAN a PCRF
- Podporuje přeposílání účtovacích zpráv pro relací založené účtování

## Související pojmy

- [TWAN – Trusted WLAN Access Network](/mobilnisite/slovnik/twan/)
- [TWAG – Trusted WLAN Access Gateway](/mobilnisite/slovnik/twag/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)

## Definující specifikace

- **TS 23.003** (Rel-19) — Numbering, addressing and identification in 3GPP
- **TS 23.273** (Rel-19) — 5G Location Services Stage 2 Architecture
- **TS 23.402** (Rel-19) — EPC for Non-3GPP Access (PMIP)
- **TS 23.852** (Rel-12) — Study on GTP-based S2a for WLAN Access
- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- **TS 29.214** (Rel-19) — Policy and Charging Control over Rx
- **TS 29.518** (Rel-19) — AMF Service Based Interface Protocol
- **TS 29.561** (Rel-19) — 5G Interworking with External Data Networks
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TS 38.413** (Rel-19) — NG Application Protocol (NGAP)

---

📖 **Anglický originál a plná specifikace:** [TWAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/twap/)
