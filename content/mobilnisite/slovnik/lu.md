---
slug: "lu"
url: "/mobilnisite/slovnik/lu/"
type: "slovnik"
title: "LU – Location Update"
date: 2025-01-01
abbr: "LU"
fullName: "Location Update"
category: "Mobility"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/lu/"
summary: "Location Update (LU) je základní procedura správy mobility, při které mobilní zařízení informuje síť o své aktuální polohové oblasti. Umožňuje síti sledovat přibližnou polohu účastníka pro efektivní d"
---

LU je základní procedura správy mobility, při které mobilní zařízení informuje síť o své aktuální polohové oblasti, aby umožnilo sledování účastníka a jeho dosažitelnost.

## Popis

Location Update (LU) je klíčová procedura v sítích 2G (GSM), 3G (UMTS) a následných 3GPP mobilních sítích, která umožňuje síti sledovat přibližnou polohu mobilní stanice ([MS](/mobilnisite/slovnik/ms/)) nebo uživatelského zařízení (UE). Je součástí vrstvy správy mobility (Mobility Management, [MM](/mobilnisite/slovnik/mm/)). Procedura je spuštěna, když UE zjistí, že vstoupilo do nové polohové oblasti (Location Area, [LA](/mobilnisite/slovnik/la/)) v okruhově přepínaných doménách nebo do nové sledovací oblasti (Tracking Area, [TA](/mobilnisite/slovnik/ta/)) v paketově přepínaných doménách EPS/5GS, nebo periodicky na základě časovače.

Z architektonického hlediska zahrnuje procedura LU signalizaci mezi UE a jádrem sítě prostřednictvím rádiové přístupové sítě. Mezi klíčové síťové komponenty patří Visitor Location Register ([VLR](/mobilnisite/slovnik/vlr/)) v okruhově přepínané doméně a Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v paketově přepínané doméně LTE/EPC. Když se UE zapne, přesune, nebo na základě časovače, odešle do sítě zprávu Location Update Request (nebo Tracking Area Update Request). Tato zpráva obsahuje identitu UE (např. [TMSI](/mobilnisite/slovnik/tmsi/) nebo [IMSI](/mobilnisite/slovnik/imsi/)) a identifikátor její předchozí polohové oblasti.

Obslužný síťový uzel (VLR/MME) následně autentizuje UE a může kontaktovat domovskou síť účastníka (HLR/HSS), aby získal data účastníka a aktualizoval ukazatel na jeho aktuální polohu. HLR/HSS zruší registraci polohy ve starém VLR/MME a vloží data účastníka do nového. Po úspěšném dokončení odešle síť UE zprávu Location Update Accept, která často přidělí novou dočasnou identitu (TMSI nebo GUTI) pro soukromí budoucí signalizace. Síť nyní ví, že UE se nachází v této konkrétní polohové nebo sledovací oblasti, a může ji tam vyvolat (paging) pro příchozí hovory nebo relace.

Fungování je založeno na konceptu oblastí. Síť je rozdělena na polohové oblasti (LAs), z nichž každá se skládá z více buněk. UE čte identifikátor LA (LAI) vysílaný na Broadcast Control Channel (BCCH). Když se LAI změní, UE iniciuje LU. Tím se vyvažuje potřeba znalosti polohy se signalizační zátěží; příliš malé oblasti způsobují časté aktualizace, zatímco příliš velké oblasti zvyšují provoz při vyvolávání. Procedura zajišťuje, že síťová databáze poloh je dostatečně přesná pro doručování služeb bez nutnosti neustálého sledování na úrovni buňky.

## K čemu slouží

Procedura Location Update byla vytvořena k vyřešení základního problému dosažitelnosti účastníka v celulární síti bez nutnosti neustálého, přesného sledování polohy. V rané mobilní telefonii potřebovala síť způsob, jak najít účastníka pro doručení příchozího hovoru. Naivní přístup by byl vyvolávat účastníka v každé buňce, což by spotřebovalo nadměrné rádiové prostředky a životnost baterie. Naopak, nesledování účastníka vůbec by znemožnilo doručení.

Mechanismus LU představil elegantní kompromis. Tím, že UE hlásí svůj pohyb mezi většími polohovými oblastmi, si síť udržuje znalost přibližné polohy účastníka (na úrovni LA). Když dorazí hovor, síť potřebuje vyvolat účastníka pouze ve všech buňkách v rámci této jedné LA, což významně snižuje signalizační režii. Tím bylo vyřešeno kritické dilema mezi efektivitou síťových prostředků a dostupností služeb. Odstranilo to omezení dřívějších primitivnějších rádiových systémů, kterým chyběla takto strukturovaná správa mobility.

Historicky, formalizovaná v GSM a přenesená přes 3GPP verze, byla procedura LU motivována potřebou automatizované, škálovatelné správy mobility s rostoucím počtem účastníků. Umožnila roaming mezi různými částmi sítě (a mezi různými sítěmi) tím, že poskytla standardizovaný způsob, jak navštívené sítě informovaly domovskou síť o přítomnosti účastníka. Vytváření dočasných identit (TMSI) během LU také zvýšilo soukromí účastníka. Její evoluce v Tracking Area Updates v LTE/5G pro paketově přepínané domény dokládá její trvalý účel: umožnit efektivní sledování zařízení pro dosažitelnost při současné optimalizaci využití rádiových a signalizačních prostředků jádra sítě.

## Klíčové vlastnosti

- Procedura pro registraci aktuální polohové/sledovací oblasti UE v síti
- Spuštěna změnou oblasti, zapnutím nebo periodickým časovačem
- Aktualizuje databáze poloh v VLR/MME a HLR/HSS
- Umožňuje efektivní vyvolávání (paging) jeho omezením na známou oblast
- Často zahrnuje přidělení nové dočasné identity účastníka (TMSI/GUTI)
- Základní prvek správy mobility a dosažitelnosti účastníka

## Související pojmy

- [TMSI – Temporary Mobile Subscriber Identifier](/mobilnisite/slovnik/tmsi/)
- [VLR – Visitor Location Register](/mobilnisite/slovnik/vlr/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)

## Definující specifikace

- **TS 21.810** (Rel-4) — Multi-mode UE Issues - Categories, principles and procedures
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 21.910** (Rel-4) — Multi-mode UE Operation Principles

---

📖 **Anglický originál a plná specifikace:** [LU na 3GPP Explorer](https://3gpp-explorer.com/glossary/lu/)
