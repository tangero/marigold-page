---
slug: "hs-gw"
url: "/mobilnisite/slovnik/hs-gw/"
type: "slovnik"
title: "HS-GW – HRPD Serving Gateway"
date: 2025-01-01
abbr: "HS-GW"
fullName: "HRPD Serving Gateway"
category: "Core Network"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/hs-gw/"
summary: "Brána jádrové sítě definovaná pro interoperabilitu mezi sítěmi 3GPP (E-UTRAN/UTRAN/GERAN) a 3GPP2 CDMA2000 HRPD (High Rate Packet Data). Slouží jako kotva mobility a brána uživatelské roviny pro termi"
---

HS-GW je brána jádrové sítě, která poskytuje kotvu mobility a uživatelskou rovinu pro interoperabilitu mezi sítěmi 3GPP a 3GPP2 CDMA2000 HRPD.

## Popis

[HRPD](/mobilnisite/slovnik/hrpd/) Serving Gateway (HS-GW) je funkční entita definovaná ve specifikacích 3GPP pro interoperabilitu s přístupem non-3GPP, konkrétně pro připojení k sítím 3GPP2 CDMA2000 1xEV-DO (Evolution-Data Optimized), známým také jako sítě HRPD (High Rate Packet Data). Je to klíčová komponenta architektury Evolved Packet Core (EPC), která umožňuje plynulý přechod a kontinuitu služeb pro uživatelské zařízení (UE) pohybující se mezi sítěmi LTE/UMTS/GSM a [CDMA](/mobilnisite/slovnik/cdma/) HRPD. HS-GW se nachází v navštívené nebo domovské [PLMN](/mobilnisite/slovnik/plmn/) a rozhraní na jedné straně komunikuje s HRPD Access Network ([AN](/mobilnisite/slovnik/an/)) a na straně druhé s 3GPP EPC. Jejími hlavními úlohami je sloužit jako lokální kotva mobility pro UE během předávání mezi oběma typy přístupu a spravovat tunelování uživatelské roviny pro datový provoz.

Z architektonického pohledu HS-GW implementuje funkce analogické jak Serving Gateway ([SGW](/mobilnisite/slovnik/sgw/)), tak Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) definované pro 3GPP přístupy, ale přizpůsobené pro rozhraní HRPD. Ukončuje specifické [GRE](/mobilnisite/slovnik/gre/) (Generic Routing Encapsulation) tunely od HRPD AN. Na straně 3GPP EPC navazuje [GTP](/mobilnisite/slovnik/gtp/) tunely S5/S8 směrem k PGW (pokud není integrována s funkcionalitou PGW) nebo sama vystupuje jako PGW (pokud je nakonfigurována jako kombinace HSGW/PGW). HS-GW také komunikuje se serverem 3GPP AAA pro autentizaci, autorizaci a účtování procedur pro UE přistupující přes HRPD. Přiděluje UE IP adresu nebo tuto funkci deleguje na PGW.

Během předávání mezi RAT z E-UTRAN do HRPD (nebo naopak) je HS-GW klíčovým uzlem. Pro předávání z LTE do HRPD (optimalizované předávání) je cílový HS-GW připraven signalizací mezi MME (Mobility Management Entity) a HS-GW přes referenční bod S101. HS-GW ustaví potřebné zdroje s HRPD AN. Když se UE připojí přes HRPD v režimu nečinnosti, HS-GW provede procedury počátečního připojení, kontaktuje 3GPP AAA a HSS k autentizaci účastníka a získání jeho profilu. Poté ustaví PDN připojení k PGW, čímž vytvoří koncový bearer pro datový provoz UE. HS-GW také provádí vynucování politik, aplikuje QoS politiky a pravidla účtování přijatá od Policy and Charging Rules Function (PCRF) přes rozhraní Gxa.

## K čemu slouží

HS-GW byla zavedena ve verzi 3GPP Release 8 spolu s počátečními specifikacemi LTE/EPC, aby řešila kritický požadavek reálného nasazení: plynulou interoperabilitu mezi novými sítěmi 3GPP LTE a široce rozšířenými legacy sítěmi 3GPP2 CDMA2000, zejména na trzích, jako je Severní Amerika, Japonsko a Jižní Korea, kde byla CDMA dominantní. Operátoři zavádějící LTE potřebovali standardizovanou a efektivní cestu, jak využít své stávající CDMA HRPD sítě pro pokrytí a záložní režim, obzvláště v počátečních fázích nasazení LTE, kdy bylo pokrytí řídké. Bez brány jako je HS-GW by byl přechod mezi těmito technologiemi omezen na jednoduché přesměrování typu 'přeruš a pak vytvoř', což by způsobilo významné přerušení služeb.

HS-GW řeší problém mobility v heterogenních sítích tím, že poskytuje jednotnou kotvu v rámci EPC pro přístupy 3GPP i HRPD. Abstrahuje specifika HRPD přístupové sítě a prezentuje ji jádru jako další IP-bázi přístupovou technologii. To umožňuje, aby klíčové funkce EPC, jako je plynulé předávání (prostřednictvím optimalizovaných procedur předávání), konzistentní vynucování politik a jednotné účtování, fungovaly přes technologickou hranici. Její vytvoření bylo motivováno potřebou architektury pro interoperabilitu s non-3GPP přístupy, která byla těsněji integrovaná než generický přístup I-WLAN, nabízející nižší latenci a lepší výkon pro předávání, což bylo zásadní pro hlasové a služby v reálném čase, jak se sítě vyvíjely směrem k VoLTE a SRVCC.

## Klíčové vlastnosti

- Kotva mobility pro předávání mezi přístupem 3GPP (LTE/UMTS) a 3GPP2 HRPD
- Ukončovací bod pro specifické GRE tunely od HRPD Access Network
- Komunikuje se serverem 3GPP AAA pro autentizaci účastníka přes HRPD
- Navazuje GTP tunely (S5/S8) směrem k PGW nebo integruje funkcionalitu PGW
- Podporuje optimalizované procedury předávání přes rozhraní S101 (signalizace) a S103 (přeposílání dat)
- Vynucuje QoS politiky a pravidla účtování přijatá od PCRF přes rozhraní Gxa

## Související pojmy

- [HRPD – High Rate Packet Data](/mobilnisite/slovnik/hrpd/)
- [SGW – Signalling Gateway](/mobilnisite/slovnik/sgw/)
- [PGW – PDN Gateway](/mobilnisite/slovnik/pgw/)
- [S101 – S101 Interface](/mobilnisite/slovnik/s101/)

## Definující specifikace

- **TS 33.402** (Rel-19) — Security for non-3GPP access to EPS

---

📖 **Anglický originál a plná specifikace:** [HS-GW na 3GPP Explorer](https://3gpp-explorer.com/glossary/hs-gw/)
