---
slug: "pch-text-pch"
url: "/mobilnisite/slovnik/pch-text-pch/"
type: "slovnik"
title: "PCH – Paging Channel"
date: 2025-01-01
abbr: "PCH"
fullName: "Paging Channel"
category: "Radio Access Network"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/pch-text-pch/"
summary: "Transportní kanál v sestupném směru v UMTS používaný k přenosu stránkovacích zpráv ze sítě do UE v režimu nečinnosti nebo připojení. Umožňuje efektivní lokalizaci UE a navázání hovoru vysíláním stránk"
---

PCH je transportní kanál v sestupném směru v UMTS, který přenáší stránkovací zprávy ze sítě do UE v režimu nečinnosti nebo připojení, aby umožnil efektivní lokalizaci a navázání hovoru.

## Popis

Stránkovací kanál ([PCH](/mobilnisite/slovnik/pch/)) je základní transportní kanál v sestupném směru v rámci rádiové přístupové sítě UMTS ([UTRAN](/mobilnisite/slovnik/utran/)), standardizovaný od verze Release 99. Funguje ve spojení s logickým kanálem Paging Control Channel ([PCCH](/mobilnisite/slovnik/pcch/)). Primární funkcí PCH je přenášet stránkovací zprávy ze sítě do uživatelských zařízení (UE), která jsou v režimu nečinnosti nebo ve stavech CELL_PCH, [URA](/mobilnisite/slovnik/ura/)_PCH či CELL_[FACH](/mobilnisite/slovnik/fach/). Tyto zprávy slouží k upozornění UE na příchozí hovory, [SMS](/mobilnisite/slovnik/sms/) zprávy nebo k vyvolání aktualizace polohové oblasti. PCH je namapován na fyzický kanál Secondary Common Control Physical Channel ([S-CCPCH](/mobilnisite/slovnik/s-ccpch/)) pro přenos na fyzické vrstvě. Klíčovým architektonickým aspektem je, že PCH podporuje vysílání v celé buňce a musí být vysílán ve všech buňkách patřících do stejné stránkovací oblasti (jako je Location Area nebo Routing Area), aby bylo zajištěno, že UE může být dosaženo bez ohledu na jeho přesnou polohu v buňce při režimu nečinnosti.

Z procedurálního hlediska síť zahajuje stránkování, když potřebuje navázat komunikaci s konkrétním UE, jehož přesná poloha v buňce není známa. Jádrová síť (CN), typicky [MSC](/mobilnisite/slovnik/msc/) nebo SGSN, odešle stránkovací požadavek do RNC. RNC následně naplánuje stránkovací zprávu na transportní kanál PCH. Zpráva obsahuje identitu UE (jako IMSI, TMSI nebo P-TMSI) a důvod stránkování. Zpracování na fyzické vrstvě zahrnuje kanálové kódování, prokládání a modulaci před přenosem na S-CCPCH. UE se periodicky probouzejí z cyklů nespojitého příjmu (DRX), aby monitorovala svůj přiřazený Paging Indicator Channel (PICH) pro rychlý indikátor; pokud je detekován pozitivní indikátor, UE následně dekóduje přidružený rámec S-CCPCH, aby přijala celou stránkovací zprávu na PCH.

Role PCH je klíčová pro efektivitu sítě a úsporu energie UE. Umožňuje síti lokalizovat a kontaktovat UE bez nutnosti, aby tato nepřetržitě naslouchala všem kanálům v sestupném směru, čímž významně prodlužuje životnost baterie. Konstrukce zajišťuje spolehlivé doručení pomocí opakování stránkování a asociace s rychlým PICH. Jeho provoz je základním kamenem správy mobility a umožňuje služby jako ukončení hlasového hovoru, SMS a zahájení paketově orientované relace. Specifikace upravující jeho charakteristiky, jako je časování a transportní formát, jsou podrobně popsány v dokumentech 3GPP TS 25.101 a TS 25.141.

## K čemu slouží

Stránkovací kanál byl vytvořen, aby vyřešil základní problém efektivního dosažení mobilního zařízení, jehož přesná poloha v buňce není síti známa, což je nezbytné pro zahájení hovorů a služeb ukončených v mobilní síti. Před vznikem celulárních systémů by jednoduché stránkování vyžadovalo vysílání zprávy po velmi rozsáhlé oblasti, což by spotřebovávalo nadměrné rádiové zdroje. V raném GSM bylo stránkování zavedeno a UMTS R99 tento koncept převzalo a přizpůsobilo pro své rozhraní založené na WCDMA. PCH v kombinaci s DRX a PICH řeší omezení neustálého monitorování UE, které by rychle vybilo baterii. Poskytuje standardizovanou, energeticky optimalizovanou metodu, jak síť může zahájit komunikaci s nečinnými UE, což je nezbytné pro jakýkoli spojově orientovaný systém mobilní telefonie. Jeho vznik byl motivován potřebou podporovat bezproblémovou mobilitu a trvalé připojení při současné prioritizaci šetření energie baterie uživatelského zařízení, což je klíčový rozlišovací znak spotřebitelských mobilních sítí.

## Klíčové vlastnosti

- Transportní kanál v sestupném směru pro přenos stránkovacích zpráv a informací o oznámeních.
- Namapován na fyzický kanál Secondary Common Control Physical Channel (S-CCPCH) pro přenos.
- Podporuje vysílání v buňce a je vyžadován ve všech buňkách stránkovací oblasti.
- Funguje ve spojení s Paging Indicator Channel (PICH) pro efektivní úsporu energie UE prostřednictvím DRX.
- Používá se ke stránkování UE v režimu nečinnosti a ve stavech RRC CELL_PCH, URA_PCH a CELL_FACH.
- Přenáší identity UE (IMSI, TMSI, P-TMSI) a informace o důvodu stránkování.

## Související pojmy

- [PICH – Paging Indication Channel](/mobilnisite/slovnik/pich/)
- [S-CCPCH – Secondary Common Control Physical Channel](/mobilnisite/slovnik/s-ccpch/)
- [PCCH – Paging Control Channel](/mobilnisite/slovnik/pcch/)
- [DRX – Discontinuous Reception](/mobilnisite/slovnik/drx/)

## Definující specifikace

- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing

---

📖 **Anglický originál a plná specifikace:** [PCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/pch-text-pch/)
