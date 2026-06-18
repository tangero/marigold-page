---
slug: "rtk"
url: "/mobilnisite/slovnik/rtk/"
type: "slovnik"
title: "RTK – Real-Time Kinematic"
date: 2025-01-01
abbr: "RTK"
fullName: "Real-Time Kinematic"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rtk/"
summary: "Vysoce přesná polohovací technika využívající měření fáze nosné vlny ze signálů GNSS, často vylepšená korekčními daty z referenční stanice nebo sítě. V 3GPP umožňuje přesnost na úrovni centimetrů pro"
---

RTK je vysoce přesná polohovací technika GNSS, která využívá měření fáze nosné vlny a korekční data k dosažení přesnosti na úrovni centimetrů pro služby, jako jsou autonomní vozidla, v rámci mobilních sítí.

## Popis

Real-Time Kinematic (RTK) je pokročilá metoda určování polohy standardizovaná v rámci 3GPP, zejména ve specifikacích jako TS 36.305 (LTE), TS 37.355 (LTE/NR), TS 38.305 (NR) a TS 38.859. Funguje porovnáním fáze nosné vlny ze signálů globálního navigačního satelitního systému ([GNSS](/mobilnisite/slovnik/gnss/)) přijímaných na pohyblivém přijímači (např. UE) s fází přijímanou na pevné referenční stanici s přesně známou polohou. Tento diferenciální přístup eliminuje společné chyby, jako je drift satelitních hodin, atmosférické zpoždění a nepřesnosti oběžných drah, což umožňuje dosažení přesnosti polohy na úrovni centimetrů v reálném čase.

Architektura pro RTK v systémech 3GPP zahrnuje několik klíčových komponent: UE (pohyblivý přijímač) vybavené přijímačem GNSS schopným sledování fáze nosné vlny, jednu nebo více referenčních stanic s přesně známými souřadnicemi a komunikační spojení – typicky poskytované mobilní sítí (LTE nebo 5G NR) – pro doručování korekčních dat. Referenční stanice vypočítá korekce chyb porovnáním své známé polohy s naměřenými daty GNSS. Tyto korekce, často formátované pomocí standardů jako RTCM (Radio Technical Commission for Maritime Services) nebo protokolů definovaných 3GPP, jsou poté přenášeny do UE prostřednictvím bod-bodových nebo broadcastových metod. UE aplikuje tyto korekce na vlastní měření GNSS, aby vypočítala vysoce přesnou polohu.

Princip fungování RTK zahrnuje, že UE provádí řešení nejednoznačnosti fáze nosné vlny, což je proces určení celočíselného počtu vlnových délek mezi satelitem a přijímačem. Po vyřešení poskytují měření fáze nosné vlny extrémně přesné informace o vzdálenosti. Standardy 3GPP definují protokoly pro doručování korekčních dat, jako je LTE Positioning Protocol ([LPP](/mobilnisite/slovnik/lpp/)) a NR Positioning Protocol (NRPP), které podporují RTK jako metodu vysoké přesnosti. Síť může UE asistovat poskytováním pomocných dat, jako je přibližná poloha, efemeridy satelitů a atmosférické modely, aby urychlila řešení nejednoznačnosti a zlepšila spolehlivost. Role RTK je nedílnou součástí podpory 5G pro ultra-spolehlivou komunikaci s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)) a komunikaci s masivním počtem zařízení (mMTC), což umožňuje přesné určování polohy pro kritické aplikace.

## K čemu slouží

RTK byla integrována do standardů 3GPP, aby uspokojila rostoucí poptávku po vysoce přesném určování polohy v komerčních a průmyslových aplikacích. Tradiční metody [GNSS](/mobilnisite/slovnik/gnss/), jako je standardní [GPS](/mobilnisite/slovnik/gps/) nebo Assisted-GPS ([A-GPS](/mobilnisite/slovnik/a-gps/)), nabízejí přesnost na úrovni metrů, což je nedostatečné pro nově vznikající případy použití, jako je autonomní řízení, precizní zemědělství, navigace dronů a rozšířená realita. Tyto aplikace vyžadují přesnost na úrovni centimetrů, aby byla zajištěna bezpečnost, efektivita a funkčnost. Omezení předchozích přístupů zahrnovala náchylnost k atmosférickým chybám, mnohocestnému rušení a potřebu dlouhých pozorovacích časů pro dosažení vysoké přesnosti.

Motivace pro její vytvoření pramení ze sbližování telekomunikačních a polohovacích technologií, které využívá všudypřítomné pokrytí a nízkolatenční konektivitu mobilních sítí k spolehlivému doručování korekčních dat RTK. Před standardizací v 3GPP systémy RTK často spoléhaly na vyhrazená rádiová spojení nebo internetová připojení, která nebyla optimalizována pro mobilitu, škálovatelnost nebo integraci s mobilními zařízeními. Standardizací podpory RTK v rámci LTE a 5G umožňuje 3GPP bezproblémové, síťově asistované určování polohy s vysokou přesností jako nativní službu, čímž snižuje náklady na nasazení a složitost.

Historicky se RTK používala v geodézii a mapování po desetiletí, ale její adopci v zařízeních pro masový trh bránily náklady a složitost přijímačů a doručování korekčních dat. Práce 3GPP, začínající v Release 15 s 5G, řeší tyto překážky definováním efektivních protokolů a síťových architektur, které podporují přenos korekčních dat s nízkou latencí přes mobilní spoje. Tím je vyřešen problém poskytování vysoce přesného určování polohy v reálném čase obrovskému počtu zařízení, což otevírá nové vertikální trhy a vylepšuje stávající služby založené na poloze s nebývalou přesností.

## Klíčové vlastnosti

- Přesnost určování polohy na úrovni centimetrů využívající měření fáze nosné vlny GNSS
- Podpora doručování diferenciálních korekčních dat prostřednictvím sítí LTE a 5G NR
- Integrace s polohovacími protokoly 3GPP, jako jsou LPP a NRPP, pro asistenční data
- Řešení nejednoznačnosti fáze nosné vlny pro přesné určení vzdálenosti
- Kompatibilita s více konstelacemi GNSS (GPS, GLONASS, Galileo, BeiDou)
- Síťové a uživatelské (UE-based) režimy určování polohy pro flexibilitu nasazení

## Související pojmy

- [GNSS – Global Navigation Satellite System](/mobilnisite/slovnik/gnss/)
- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)

## Definující specifikace

- **TS 36.305** (Rel-19) — UE Positioning in E-UTRAN Stage 2
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2
- **TR 38.859** (Rel-18) — Technical Report

---

📖 **Anglický originál a plná specifikace:** [RTK na 3GPP Explorer](https://3gpp-explorer.com/glossary/rtk/)
