---
slug: "e-stn-dr"
url: "/mobilnisite/slovnik/e-stn-dr/"
type: "slovnik"
title: "E-STN-DR – Emergency Session Transfer Number for DRVCC"
date: 2025-01-01
abbr: "E-STN-DR"
fullName: "Emergency Session Transfer Number for DRVCC"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/e-stn-dr/"
summary: "Specifické telefonní číslo používané v IMS ke směrování požadavku na přenos relace pro tísňové volání během Dual Radio Voice Call Continuity (DRVCC). Jednoznačně identifikuje funkci Emergency Access T"
---

E-STN-DR je telefonní číslo používané v IMS ke směrování požadavku na přenos relace pro tísňové volání během DRVCC, které jednoznačně identifikuje E-ATCF, který kotví relaci pro přenos mezi přístupovými sítěmi.

## Popis

Emergency Session Transfer Number for [DRVCC](/mobilnisite/slovnik/drvcc/) (E-STN-DR) je klíčový směrovací identifikátor v architektuře IMS (IP Multimedia Subsystem) pro kontinuitu tísňových služeb. Používá se konkrétně v kontextu Dual Radio Voice Call Continuity (DRVCC), což je scénář, kdy je uživatelské zařízení (UE) schopno současně udržovat připojení na paketově spínaném (PS) přístupu (jako LTE nebo 5G NR) i na okruhově spínaném ([CS](/mobilnisite/slovnik/cs/)) přístupu (jako GSM nebo UMTS). Když takové UE s aktivním tísňovým IMS hlasovým hovorem potřebuje předat hovor z PS domény do CS domény (nebo naopak), je E-STN-DR klíčem, který na IMS vrstvě iniciuje přenos relace.

Technicky je E-STN-DR tel URI (např. tel:+1234567890) nakonfigurované v síti a asociované s funkcí Emergency Access Transfer Control Function (E-ATCF). E-ATCF je IMS entita, která kotví tísňový hovor za účelem kontinuity služby. Když je vyžadován DRVCC přenos pro tísňový hovor, UE nebo síť zahájí proceduru přenosu IMS relace. To zahrnuje odeslání požadavku SIP INVITE nebo REFER obsahujícího E-STN-DR v Request-URI nebo Refer-To hlavičce. Jádrová síť IMS směruje tento požadavek na základě čísla E-STN-DR přímo ke konkrétní E-ATCF, která kotví původní tísňový hovor.

Po přijetí požadavku E-ATCF jej korelovala s existující tísňovou IMS relací pomocí identifikátorů uložených během sestavování hovoru. Poté provede procedury Access Transfer, které zahrnují aktualizaci mediální cesty vzdáleného konce (např. Public Safety Answering Point nebo jiného UE), aby ukazovala ze starého přístupového spoje (PS) na nový přístupový spoj (CS). Tím je zajištěno nepřerušené pokračování mediálního toku na novém síťovém nosiči. E-STN-DR se liší od [E-STN-SR](/mobilnisite/slovnik/e-stn-sr/) používaného pro Single Radio VCC, protože procedury DRVCC mohou být iniciovány později během hovoru a zahrnují odlišné schopnosti zařízení. Jeho definice a použití jsou rozprostřeny napříč specifikacemi jako TS 23.237 (VCC), 23.271 (služby polohy) a 23.771 (rozšířené VCC).

## K čemu slouží

E-STN-DR byl zaveden ve 3GPP Release 13, aby rozšířil robustní podporu kontinuity tísňových hovorů na zařízení s duální rádiovou schopností. Předchozí standardy definovaly [E-SR-VCC](/mobilnisite/slovnik/e-sr-vcc/) a s ním spojené [E-STN-SR](/mobilnisite/slovnik/e-stn-sr/) pro zařízení s jedním rádiem, která musí přerušit PS připojení před navázáním [CS](/mobilnisite/slovnik/cs/) připojení. Zařízení s nezávislými transceivery (běžné u prvních telefonů s podporou VoLTE, které měly také 3G rádia) však mohla používat [DRVCC](/mobilnisite/slovnik/drvcc/), který umožňuje plynulejší přenos typu 'make-before-break'. Stávající mechanismy kontinuity pro tísňové hovory nebyly pro tento scénář s duálním rádiem plně definovány.

Zavedení E-STN-DR vyřešilo problém, jak jednoznačně a spolehlivě identifikovat a směrovat požadavek na přenos relace pro *tísňový* hovor v kontextu DRVCC. Bez vyhrazeného čísla pro tísňové volání by síť nemohla rozlišit mezi běžným DRVCC přenosem a kritickým přenosem tísňového hovoru, což by mohlo vést k nesprávnému směrování nebo nedostatku prioritního zpracování. Definováním E-STN-DR zajistilo 3GPP, že procedury DRVCC pro tísňové hovory budou vždy směrovány ke správné E-ATCF, která je zřízena pro zpracování specifických regulatorních a prioritních aspektů tísňových relací, čímž se zachovává stejná vysoká spolehlivost tísňových služeb na pokročilých zařízeních s duálním rádiem jako na zařízeních s jedním rádiem.

## Klíčové vlastnosti

- Unikátní telefonní číslo (Tel URI) používané ke směrování požadavků IMS na přenos relace pro tísňové hovory
- Specificky navrženo pro scénáře Dual Radio Voice Call Continuity (DRVCC)
- Globálně směruje k funkci Emergency Access Transfer Control Function (E-ATCF) kotvící hovor
- Umožňuje přenos typu 'make-before-break' pro tísňové hovory na UE s duálním rádiem
- Odlišné od E-STN-SR používaného pro Single Radio VCC (SR-VCC)
- Spouštěno prostřednictvím SIP INVITE/REFER během procedury přenosu přístupu v IMS

## Související pojmy

- [DRVCC – Dual Radio Voice Call Continuity](/mobilnisite/slovnik/drvcc/)
- [E-SR-VCC – Emergency Single Radio Voice Call Continuity](/mobilnisite/slovnik/e-sr-vcc/)
- [E-STN-SR – Emergency Call Session Transfer Number – Single Radio](/mobilnisite/slovnik/e-stn-sr/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 23.237** (Rel-19) — IMS Service Continuity (ISC) Stage 2
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.771** (Rel-13) — IMS Emergency Sessions over WLAN Study

---

📖 **Anglický originál a plná specifikace:** [E-STN-DR na 3GPP Explorer](https://3gpp-explorer.com/glossary/e-stn-dr/)
