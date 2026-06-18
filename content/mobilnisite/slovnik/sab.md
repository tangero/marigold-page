---
slug: "sab"
url: "/mobilnisite/slovnik/sab/"
type: "slovnik"
title: "SAB – Service Area Broadcast"
date: 2025-01-01
abbr: "SAB"
fullName: "Service Area Broadcast"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sab/"
summary: "Služba vysílání buňkou (cell broadcast service) v UMTS, která distribuuje informace (např. zprávy, dopravní upozornění) všem uživatelům ve specifické geografické servisní oblasti. Umožňuje efektivní š"
---

SAB je služba vysílání buňkou (cell broadcast service) v UMTS, která distribuuje informace všem uživatelům ve specifické geografické oblasti za účelem efektivního šíření místních informací v režimu jeden-všem.

## Popis

Service Area Broadcast (SAB) je služba vysílání buňkou definovaná ve specifikacích 3GPP pro UMTS, navržená pro efektivní simultánní doručování informací více uživatelským zařízením (UE) v definované geografické oblasti, známé jako Servisní oblast (Service Area). Na rozdíl od unicastových služeb, které navazují individuální spojení s každým příjemcem, SAB funguje na principu jeden-všem, což ji činí vysoce efektivní pro šíření neinteraktivních, lokálně relevantních informací. Služba se typicky používá pro vysílání veřejných informací, jako jsou dopravní a meteorologická upozornění, titulek zpráv, burzovní tickery nebo místní reklama, na všechna kompatibilní mobilní zařízení v cílové zóně.

Architektura SAB zahrnuje několik síťových prvků. Hlavní komponentou je Cell Broadcast Centre ([CBC](/mobilnisite/slovnik/cbc/)), které je zodpovědné za přijímání vysílacích zpráv od poskytovatelů obsahu nebo operátorů sítě. CBC tyto zprávy zpracovává, určuje jejich geografický rozsah (seznam buněk nebo Servisních oblastí) a plánování. V architektuře UMTS CBC komunikuje s jádrem sítě, konkrétně s [MSC](/mobilnisite/slovnik/msc/) nebo [SGSN](/mobilnisite/slovnik/sgsn/) (pro GSM/UMTS), pomocí Cell Broadcast Protocolu. Pro UMTS jsou vysílané informace směrovány přes rozhraní lu-BC k Radiovému síťovému řadiči ([RNC](/mobilnisite/slovnik/rnc/)). RNC je klíčový prvek, protože spravuje rádiové zdroje pro vysílání. Používá protokol Cell Broadcast Service ([CBS](/mobilnisite/slovnik/cbs/)) přes rozhraní lu-BC a mapuje vysílané zprávy na společné transportní kanály rozhraní vzduchu, konkrétně na Forward Access Channel ([FACH](/mobilnisite/slovnik/fach/)) nebo na vyhrazený vysílací kanál Broadcast Control Channel ([BCCH](/mobilnisite/slovnik/bcch/)) v režimu nečinnosti (idle mode) či na Common Traffic Channel ([CTCH](/mobilnisite/slovnik/ctch/)) v režimu připojení (connected mode).

Fungování SAB začíná vytvořením zprávy a geografickým cílením v CBC. Jakmile je zpráva naplánována pro konkrétní Servisní oblast (což může být jedna buňka, skupina buněk nebo větší region), CBC ji odešle příslušným RNC. RNC následně naplánuje vysílání přes rádiové rozhraní pomocí opakovaného přenosového vzoru, aby zajistilo, že UE, která byla dočasně mimo dosah nebo vypnutá, mají šanci zprávu přijmout. Na straně UE musí mít mobilní zařízení povolenou a nakonfigurovanou schopnost SAB pro příjem specifických identifikátorů zpráv (Message IDs) a geografických kódů. UE kontinuálně monitoruje určený vysílací kanál, filtruje zprávy na základě svých předplatných a polohy a relevantní vysílání zobrazuje uživateli. Služba funguje na principu 'push' bez požadavku nebo potvrzení od UE, čímž šetří síťové i zařízení zdroje. Její integrace do UMTS vyžadovala specifické protokoly na rozhraní lu-BC a podporu v protokolu RRC pro konfiguraci a příjem vysílacího kanálu.

## K čemu slouží

Service Area Broadcast byl vytvořen, aby poskytl standardizovaný, síťově efektivní mechanismus pro doručování lokalizovaných informací masovému publiku v rámci mobilní sítě. Před jeho standardizací měli operátoři omezené možnosti pro zasílání společných informací mnoha uživatelům, často museli sáhnout k neefektivnímu hromadnému rozesílání SMS všem účastníkům v regionu, což spotřebovávalo značné signalizační a přenosové zdroje. SAB tento problém řeší využitím inherentních vysílacích schopností rádiového rozhraní, což umožňuje, aby jediný přenos ze sítě přijal neomezený počet UE v rádiovém dosahu, což dramaticky zlepšuje spektrální efektivitu pro distribuci dat v režimu jeden-všem.

Historický kontext spočívá ve vývoji přidaných služeb nad rámec hlasu. Jak se mobilní telefony staly všudypřítomnými, rostla poptávka po službách založených na poloze. SAB byl motivován případy užití jako jsou systémy veřejného varování (např. před přírodními katastrofami), dopravní informace pro řidiče a komerční vysílání. Řešil omezení služeb typu bod-bod pro hromadná oznámení tím, že poskytl řízený, operátorem spravovaný vysílací kanál. Jeho vytvoření v 3GPP Rel-4 formalizovalo a vylepšilo službu Cell Broadcast Service (CBS) z GSM pro prostředí UMTS, což zajistilo konzistentní nabídku služeb napříč sítěmi 2G a 3G a umožnilo nové zdroje příjmů a aplikace veřejných služeb pro síťové operátory.

## Klíčové vlastnosti

- Distribuce informací v režimu jeden-všem bez individuální adresace nebo potvrzení
- Geografické cílení na specifické Servisní oblasti (buňka, skupina buněk nebo region)
- Využívá společné rádiové kanály (např. FACH, CTCH) pro efektivní využití spektra
- Založeno na push modelu s opakovaným vysíláním pro zajištění příjmu
- Vyžaduje Cell Broadcast Centre (CBC) pro vytváření a správu zpráv
- UE se přihlašuje k odběru specifických typů zpráv pomocí Message IDs pro filtrování

## Související pojmy

- [CBS – Cell Broadcast Service](/mobilnisite/slovnik/cbs/)
- [CTCH – Common Traffic Channel](/mobilnisite/slovnik/ctch/)
- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)

## Definující specifikace

- **TS 25.401** (Rel-19) — UTRAN Overall Architecture

---

📖 **Anglický originál a plná specifikace:** [SAB na 3GPP Explorer](https://3gpp-explorer.com/glossary/sab/)
