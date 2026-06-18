---
slug: "r-tpdu"
url: "/mobilnisite/slovnik/r-tpdu/"
type: "slovnik"
title: "R-TPDU – Response Transport Protocol Data Unit"
date: 2025-01-01
abbr: "R-TPDU"
fullName: "Response Transport Protocol Data Unit"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/r-tpdu/"
summary: "Jednotka dat transportního protokolu (TPDU) odeslaná jako odpověď na požadavek, která tvoří část dialogu v různých signalizačních protokolech 3GPP. Je základní zprávovou konstrukcí používanou k přenos"
---

R-TPDU (jednotka dat transportního protokolu typu odpověď) je jednotka dat transportního protokolu odeslaná jako odpověď na požadavek, používaná v signalizačních protokolech 3GPP, jako je TCAP, k přenosu potvrzení, výsledků nebo dat mezi síťovými entitami.

## Popis

Response Transport Protocol Data Unit (R-TPDU) je specifický typ paketu definovaný v rámci signalizačních protokolů 3GPP, které využívají transakční model požadavek-odpověď. Je protějškem k [TPDU](/mobilnisite/slovnik/tpdu/) typu Begin nebo Query a nese výsledek, potvrzení nebo požadované informace zpět k iniciující entitě. R-TPDU jsou nedílnou součástí protokolů, jako je Transaction Capabilities Application Part ([TCAP](/mobilnisite/slovnik/tcap/)), který poskytuje standardizovaný způsob komunikace a provádění vzdálených operací mezi aplikacemi v různých síťových uzlech (např. [MSC](/mobilnisite/slovnik/msc/), [HLR](/mobilnisite/slovnik/hlr/), [SCP](/mobilnisite/slovnik/scp/)). Struktura R-TPDU zahrnuje hlavičku identifikující ji jako odpověď a datovou část obsahující komponenty jako návratový výsledek, návratovou chybu nebo indikaci odmítnutí.

Z architektonického pohledu, když aplikace vyvolá vzdálenou operaci, spustí vytvoření dialogu řízeného TCAP. Iniciující uzel odešle TPDU (často Begin nebo Query s komponentami Invoke) k zahájení transakce. Příjemce požadavek zpracuje a vytvoří R-TPDU, které je následně přeneseno zpět k původci. Toto R-TPDU ukončí transakci nebo v ní pokračuje, pokud je potřeba další interakce. Komponenty v datové části R-TPDU jsou kódovány pomocí pravidel Abstract Syntax Notation One (ASN.1), což zajišťuje konzistentní a jednoznačnou interpretaci dat napříč různými implementacemi od výrobců.

Jak to funguje, zahrnuje vrstvený protokolový zásobník. Na vrstvě TCAP je R-TPDU sestaveno, včetně transakčních ID pro korelaci odpovědi s původním požadavkem a příslušných informací o výsledku/chybě. Tato TPDU je pak předána podkladovým transportním vrstvám signalizace, jako je Signaling Connection Control Part ([SCCP](/mobilnisite/slovnik/sccp/)) a Message Transfer Part ([MTP](/mobilnisite/slovnik/mtp/)) v sítích [SS7](/mobilnisite/slovnik/ss7/), nebo adaptacím SIGTRAN pro IP sítě. Role R-TPDU je klíčová pro dokončení signalizačních procedur, jako je správa mobility (např. aktualizace polohy), řízení hovorů a aktivace doplňkových služeb. Poskytuje mechanismus pro potvrzení úspěchu, doručení výsledků dotazu (např. data účastníka) nebo nahlášení selhání, čímž umožňuje stavové a spolehlivé interakce, které jsou páteří signalizace telekomunikační jádrové sítě.

## K čemu slouží

R-TPDU existuje jako základní prvek strukturovaných signalizačních dialogů, který zajišťuje spolehlivou a jednoznačnou komunikaci mezi distribuovanými síťovými funkcemi. V rané telekomunikační signalizaci vedly ad-hoc formáty zpráv k problémům s interoperabilitou a složitému zpracování chyb. Vývoj standardizovaných transakčně orientovaných protokolů, jako je TCAP, s jasně definovanými typy TPDU, jako je R-TPDU, byl motivován potřebou jednotné metody pro zpracování vzdálených operací a dotazů napříč sítěmi více výrobců. Řeší problém, jak spolehlivě doručit výsledek požadavku – ať už jde o data, potvrzení nebo chybový stav – zpět žadateli.

Historicky, jak se sítě vyvíjely od jednoduchého navazování hovorů k inteligentním sítím (IN) nabízejícím komplexní služby, jako je bezplatné volání nebo předplacené služby, se signalizace stávala více konverzační. Na jediný požadavek často byla potřeba podrobná odpověď obsahující data nebo vyžadující další interakci. R-TPDU jako součást sady protokolů TCAP, zavedené v éře GSM a používané dále přes UMTS a další, poskytlo tento standardizovaný kontejner pro odpovědi. Odstraňuje omezení jednoduchých potvrzovacích zpráv tím, že umožňuje zapouzdřit bohatý strukturovaný obsah (výsledky, chyby, parametry) a korelovat jej s konkrétním transakčním ID. To umožňuje provádění sofistikované servisní logiky napříč síťovými uzly a je nezbytné pro škálovatelnost a spolehlivost signalizace jádrové sítě ve 2G, 3G, 4G a dokonce i v scénářích propojení v 5G.

## Klíčové vlastnosti

- Standardizovaný typ TPDU pro odpovědi signalizačních protokolů
- Ukončuje nebo pokračuje v transakci TCAP dialogu
- Nese komponenty datové části, jako je návratový výsledek, návratová chyba nebo odmítnutí
- Obsahuje transakční ID pro korelaci s iniciujícím požadavkem
- Kódováno pomocí ASN.1 pro interoperabilitu
- Přenášeno přes sítě SS7 (SCCP/MTP) nebo IP (SIGTRAN)

## Související pojmy

- [TCAP – Transaction Capabilities Application Part](/mobilnisite/slovnik/tcap/)
- [SCCP – Signalling Connection Control Part](/mobilnisite/slovnik/sccp/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [R-TPDU na 3GPP Explorer](https://3gpp-explorer.com/glossary/r-tpdu/)
