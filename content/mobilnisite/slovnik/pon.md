---
slug: "pon"
url: "/mobilnisite/slovnik/pon/"
type: "slovnik"
title: "PON – Passive Optical Network"
date: 2025-01-01
abbr: "PON"
fullName: "Passive Optical Network"
category: "Other"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pon/"
summary: "Telekomunikační technologie využívající optická vlákna pro širokopásmový přístup, která pomocí neaktivních (nepájivých) optických rozdělovačů umožňuje, aby jediné optické vlákno obsluhovalo více konco"
---

PON (pasivní optická síť) je širokopásmová přístupová technologie využívající optická vlákna, která pomocí pasivních optických rozdělovačů umožňuje, aby jediné vlákno obsluhovalo více koncových bodů; je integrována v 3GPP pro přenos v přístupové části (fronthaul) a propojovací části (backhaul) mobilních sítí.

## Popis

Pasivní optická síť (PON) je architektura přístupové sítě typu bod–více bodů využívající optická vlákna, která je v 3GPP definována jako možnost přenosové technologie. Využívá pasivní optické rozdělovače a kombinátory v optické distribuční síti (ODN), což znamená, že mezi ústřednou a koncovým bodem zákazníka nejsou žádné aktivní elektronické komponenty. To výrazně snižuje spotřebu energie a náklady na údržbu. Systém 3GPP s PON interaguje jako se spravovanou přenosovou vrstvou, často pro propojování uzlů rádiové přístupové sítě (RAN), jako jsou distribuované jednotky ([DU](/mobilnisite/slovnik/du/)) a centralizované jednotky ([CU](/mobilnisite/slovnik/cu/)) v architektuře Cloud RAN, nebo pro zajištění backhaulu pro pevný bezdrátový přístup.

Architektura se skládá z optické linkové terminály (OLT) v ústředně poskytovatele služeb a z více optických síťových jednotek (ONU) neboli optických síťových terminálů (ONT) na straně uživatele. Jediné optické vlákno z OLT vede k pasivnímu rozdělovači v blízkosti uživatelů, který rozděluje optický výkon do více vláken napájejících ONU. Provoz ve směru downstream je vysílán z OLT ke všem ONU, přičemž každá ONU filtruje data určená pro jiné uživatele na základě identifikátorů. Provoz ve směru upstream využívá vícepřístupový protokol, typicky vícečetný přístup s časovým dělením ([TDMA](/mobilnisite/slovnik/tdma/)), kdy OLT přiděluje každé ONU konkrétní časové sloty, aby se zabránilo kolizím na sdíleném upstream kanálu.

Specifikace 3GPP (např. TS 21.866, 29.561) definují požadavky a aspekty správy pro integraci PON přenosu se systémy 5G. To zahrnuje definici monitorování výkonu, dodávání synchronizace (např. pro fronthaul CPRI nebo eCPRI) a rozhraní pro správu mezi systémem správy sítě 3GPP a systémem PON. PON je považována za přenosovou síť vrstvy 1/vrstvy 2, která musí splňovat přísné požadavky na latenci, chvění (jitter) a šířku pásma, zejména při použití pro fronthaul v disintegrovaných nasazeních RAN. Specifikace pro správu, jako je TS 32.833, pokrývají integraci správy prvků PON do širšího rámce správy 3GPP.

## K čemu slouží

Technologie PON byla integrována do standardů 3GPP, aby poskytla vysokokapacitní, nákladově efektivní a energeticky úsporné přenosové řešení pro zahušťování mobilní sítě a konvergenci pevných a mobilních sítí. Exponenciální růst mobilního datového provozu, zejména s 5G, vyžadoval nová řešení pro backhaul a fronthaul s mnohem větší kapacitou a nižší latencí než tradiční metalické nebo mikrovlnné spoje. PON, již široce nasazená pro služby fiber-to-the-home (FTTH), nabídla snadno dostupnou infrastrukturu, kterou bylo možné využít pro mobilní přenos.

Předchozí přístupy k připojení lokalit buněk často spoléhaly na aktivní metalické spoje bod–bod nebo mikrovlny, jejichž škálování mohlo být nákladné. Pasivní povaha PON snižuje provozní náklady a energetické nároky v distribučních bodech. Pro 5G architektury, jako je Cloud RAN, kde je rádiová jednotka ([RU](/mobilnisite/slovnik/ru/)) oddělena od jednotky základního pásma ([DU](/mobilnisite/slovnik/du/)/[CU](/mobilnisite/slovnik/cu/)) fronthaul spojem, PON poskytuje sdílenou optickou infrastrukturu, která může efektivně agregovat provoz z více RU. Její standardizace v rámci 3GPP zajišťuje, že mobilní operátoři mohou spravovat rádiovou i přenosovou vrstvu jednotným způsobem, což umožňuje automatizované zřizování, zajištění výkonu a správu poruch pro end-to-end síťové řezy, které mohou procházet přes PON spoje.

## Klíčové vlastnosti

- Architektura bod–více bodů využívající pasivní optické rozdělovače
- Vysoká přenosová kapacita podporující požadavky mobilního fronthaulu a backhaulu
- Vícečetný přístup s časovým dělením (TDMA) pro řízení provozu ve směru upstream
- Integrovaná správa a monitorování výkonu definované ve specifikacích 3GPP
- Podporuje přesné dodávání synchronizace pro koordinaci RAN
- Umožňuje nákladově efektivní sdílení optických vláken pro zahušťování sítě

## Definující specifikace

- **TR 21.866** (Rel-15) — Study on Energy Efficiency in 3GPP Standards
- **TS 29.214** (Rel-19) — Policy and Charging Control over Rx
- **TS 29.514** (Rel-19) — 5G System; Policy Authorization Service; Stage 3
- **TS 29.561** (Rel-19) — 5G Interworking with External Data Networks
- **TS 32.833** (Rel-11) — Converged OSS End-to-End Management Study

---

📖 **Anglický originál a plná specifikace:** [PON na 3GPP Explorer](https://3gpp-explorer.com/glossary/pon/)
