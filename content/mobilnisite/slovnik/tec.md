---
slug: "tec"
url: "/mobilnisite/slovnik/tec/"
type: "slovnik"
title: "TEC – Total Electron Content"
date: 2025-01-01
abbr: "TEC"
fullName: "Total Electron Content"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tec/"
summary: "Total Electron Content (TEC) je míra celkového počtu volných elektronů integrovaných podél dráhy zemskou ionosférou, vyjádřená v TEC jednotkách (TECU). V 3GPP se používá pro vylepšení polohování GNSS,"
---

TEC (celkový obsah elektronů) je celkový počet volných elektronů integrovaných podél dráhy zemskou ionosférou. V rámci 3GPP se používá ke korekci zpoždění signálů GNSS za účelem zvýšení přesnosti určování polohy.

## Popis

Total Electron Content (TEC) je geofyzikální parametr představující sloupcovou hustotu volných elektronů v ionosféře. Je definován jako integrál elektronové hustoty podél přímé dráhy od družice globálního navigačního satelitního systému ([GNSS](/mobilnisite/slovnik/gnss/)) k přijímači na zemském povrchu nebo v jeho blízkosti. Standardní jednotkou je TEC jednotka ([TECU](/mobilnisite/slovnik/tecu/)), kde 1 TECU = 10^16 elektronů na metr čtvereční. Ionosféra je disperzní prostředí pro rádiové signály ve frekvenčních pásmech používaných GNSS (jako [GPS](/mobilnisite/slovnik/gps/), Galileo), což znamená, že způsobuje frekvenčně závislé zpoždění šíření signálu. Toto ionosférické zpoždění je hlavním zdrojem chyby v samostatném polohování GNSS.

V kontextu 3GPP se data TEC využívají v rámci polohových služeb ([LCS](/mobilnisite/slovnik/lcs/)), konkrétně pro Assisted-GNSS ([A-GNSS](/mobilnisite/slovnik/a-gnss/)) a Advanced A-GNSS. Síť (např. polohový server jako Enhanced Serving Mobile Location Centre - [E-SMLC](/mobilnisite/slovnik/e-smlc/) nebo Location Management Function - [LMF](/mobilnisite/slovnik/lmf/)) může poskytnout asistenční data uživatelskému zařízení (UE) pro zlepšení rychlosti a přesnosti určení polohy. Tato asistenční data mohou zahrnovat ionosférické modely nebo korekce, které jsou odvozeny z měření TEC. Síť odhadne TEC pro oblast relevantní pro UE, často s využitím dat z referenčních sítí přijímačů GNSS. Poté vypočítá a přenese korekční parametry, jako jsou koeficienty pro model Klobuchar nebo pokročilejší model NeQuick, které UE aplikuje na svá měření GNSS, aby kompenzovala ionosférické zpoždění.

Specifikace asistenčních dat souvisejících s TEC je popsána v dokumentech 3GPP TS 36.305 ([E-UTRAN](/mobilnisite/slovnik/e-utran/) Stage 2 - UE positioning), TS 37.355 (LTE Positioning Protocol - LPP) a TS 38.305 (NG-RAN Stage 2 - UE positioning). Tyto dokumenty definují formátování, přenos a aplikaci modelů TEC. Proces zahrnuje žádost UE nebo poskytnutí ionosférického modelu platného pro konkrétní geografickou oblast a čas ze strany sítě. UE tento model použije ke korekci měření pseudovzdáleností od více družic, čímž výrazně sníží chybu určení polohy, která bez korekce může činit desítky metrů, na několik metrů nebo méně.

## K čemu slouží

Začlenění modelování TEC do standardů 3GPP řeší kritickou potřebu vysoce přesných a spolehlivých polohovacích služeb, které jsou povinné pro nouzová volání (např. E-911, E-112) a jsou zásadní pro řadu komerčních aplikací, jako je navigace, sledování majetku a polohově cílená reklama. Samostatné přijímače GNSS, zejména v spotřebitelských zařízeních s malými anténami, trpí významnými chybami způsobenými variabilitou ionosféry, která se mění v závislosti na denní době, sluneční aktivitě a zeměpisné poloze.

Předchozí přístupy v raném A-GNSS primárně poskytovaly efemeridní a almanachová data družic pro zkrácení času do prvního určení polohy (TTFF). Nabízely však omezenou korekci atmosférických chyb. Zavedení standardizované ionosférické korekce založené na TEC v 3GPP, zejména od vydání 16, bylo motivováno požadavkem na přesnost na úrovni metrů. Řeší problém, kdy UE potřebuje jasný a trvalý výhled na více družic, aby si mohla vypočítat vlastní ionosférický model, což je nepraktické v městských kaňonech nebo uvnitř budov. Tím, že síť vypočítá a doručí regionálně specifické modely TEC, může UE dosáhnout rychlejšího a přesnějšího určení polohy i v náročných podmínkách. Tento přístup využívá schopnost sítě agregovat data z více zdrojů a vytvořit přesnější a aktuálnější obraz ionosféry, než by mohlo jakékoli jednotlivé zařízení.

## Klíčové vlastnosti

- Geofyzikální míra elektronové hustoty v ionosféře podél dráhy signálu.
- Používá se k modelování a korekci zpoždění šíření signálu GNSS.
- Vyjádřeno v TEC jednotkách (TECU).
- Doručováno jako asistenční data prostřednictvím protokolů, jako je LPP, do UE.
- Zvyšuje přesnost polohování Assisted-GNSS (A-GNSS).
- Specifikováno v 3GPP pro polohovací architektury LTE a NR.

## Definující specifikace

- **TS 36.305** (Rel-19) — UE Positioning in E-UTRAN Stage 2
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2

---

📖 **Anglický originál a plná specifikace:** [TEC na 3GPP Explorer](https://3gpp-explorer.com/glossary/tec/)
