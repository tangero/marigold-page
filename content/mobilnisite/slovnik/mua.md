---
slug: "mua"
url: "/mobilnisite/slovnik/mua/"
type: "slovnik"
title: "MUA – Modify UE Context Answer"
date: 2025-01-01
abbr: "MUA"
fullName: "Modify UE Context Answer"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mua/"
summary: "MUA je zpráva protokolu Diameter používaná v architektuře 3GPP Policy and Charging Control (PCC). Je odeslána funkcí Policy and Charging Rules Function (PCRF) do funkce Traffic Detection Function (TDF"
---

MUA je zpráva protokolu Diameter odeslaná z PCRF do TDF pro potvrzení uplatnění aktualizovaných pravidel politiky a účtování pro uživatelskou relaci.

## Popis

Modify UE Context Answer (MUA) je příkaz protokolu Diameter (konkrétně zpráva typu Diameter Answer) definovaný na referenčních bodech Gx a Sd v rámci architektury 3GPP Policy and Charging Control ([PCC](/mobilnisite/slovnik/pcc/)). Funguje jako odpověď na Modify UE Context Request ([MUR](/mobilnisite/slovnik/mur/)). Hlavními aktéry jsou Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)), která MUA odesílá, a Traffic Detection Function ([TDF](/mobilnisite/slovnik/tdf/)) nebo Policy and Charging Enforcement Function ([PCEF](/mobilnisite/slovnik/pcef/)) rozšířená o schopnosti Application Detection and Control ([ADC](/mobilnisite/slovnik/adc/)), která ji přijímá. Tato výměna je součástí dynamického řízení relace politiky.

Její funkce je nedílnou součástí životního cyklu PCC relace. Když se PCRF rozhodne upravit politiky platné pro zavedenou uživatelskou relaci – například z důvodu změny úrovně předplatitele, detekce nové aplikace nebo požadavku od Application Function ([AF](/mobilnisite/slovnik/af/)) – odešle MUR do TDF. TDF tento požadavek, který obsahuje aktualizovaná PCC pravidla, spouštěcí události nebo ADC pravidla, zpracuje. TDF následně tato nová pravidla implementuje (např. zahájí detekci nové aplikace, použije jiné parametry účtování nebo povolí směrování provozu). Jakmile TDF změny úspěšně uplatní, odešle zpět do PCRF zprávu MUA. Zpráva MUA obsahuje [AVP](/mobilnisite/slovnik/avp/) Result-Code udávající úspěch nebo selhání a může obsahovat specifická AVP (Attribute-Value Pairs) pro hlášení stavu nebo poskytnutí aktualizovaných informací o relaci.

Její úloha v síti spočívá v poskytování spolehlivého, potvrzeného zřizování politik. Handshake typu request-answer zajišťuje, že PCRF a TDF udržují synchronizovaný stav pro uživatelskou relaci. To je klíčové pro konzistentní vynucování politik, přesné účtování a garantovanou Quality of Service (QoS). MUA potvrzuje, že vynucovací bod zavedl nová pravidla politiky do svého lokálního kontextu, což umožňuje PCRF pokračovat v dalších operacích nebo zaznamenat transakci pro audit a účtovací záznamy. Je to klíčový mechanismus, který síti umožňuje dynamicky se přizpůsobovat měnícím se podmínkám na úrovni jednotlivého předplatitele a relace.

## K čemu slouží

Zpráva MUA existuje k dokončení a potvrzení dynamické modifikace pravidel politiky pro uživatelskou relaci v rámci PCC architektury. Před PCC bylo řízení politiky statičtější, často zřizované v síťových prvcích při zahájení relace. Vývoj směrem k real-time, aplikací řízeným službám vyžadoval mechanismus pro spolehlivé zasílání aktualizací politik během relace z centrálního řadiče politik (PCRF) do vynucovacích bodů.

Řeší problém synchronizace stavu mezi řídicí rovinou (PCRF) a vynucovacími body v uživatelské rovině (TDF/PCEF). Bez potvrzující odpovědi jako je MUA by PCRF neměla žádnou záruku, že její aktualizace politik byly úspěšně nainstalovány. To by mohlo vést k nekonzistentnímu poskytování služeb (např. prémiový video stream by nedostal slíbenou QoS) nebo nesrovnalostem v účtování. MUA poskytuje potřebné potvrzení, čímž činí transakci aktualizace politik spolehlivou.

Její vznik byl motivován zavedením Traffic Detection Function (TDF) ve verzi 11, která oddělila hlubokou kontrolu paketů a detekci aplikací od PCEF. To vyžadovalo vyhrazený protokolový dialog (přes referenční bod Sd) pro správu ADC pravidel. MUA jako součást tohoto dialogu umožňuje PCRF dynamicky řídit, které aplikace jsou detekovány a jaké politiky se na ně vztahují, čímž podporuje sofistikované služební plány jako sponzorovaná data, QoS zvýšení pro konkrétní aplikace nebo rodičovské kontroly. Odstraňuje omezení statické konfigurace tím, že umožňuje síti reagovat v reálném čase na chování uživatele a politiky poskytovatele služeb.

## Klíčové vlastnosti

- Zpráva typu Diameter Answer (kód příkazu 8388622) na referenčních bodech Gx/Sd.
- Odesílána PCRF jako odpověď na Modify UE Context Request (MUR).
- Obsahuje AVP Result-Code pro indikaci úspěchu (DIAMETER_SUCCESS) nebo konkrétních chyb.
- Dokončuje aktualizaci PCC pravidel, ADC pravidel nebo spouštěcích událostí pro uživatelskou relaci.
- Zajišťuje spolehlivou synchronizaci stavu mezi PCRF a TDF/PCEF.
- Nedílná součást dynamického řízení relace politiky a účtování.

## Související pojmy

- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [TDF – Traffic Detection Function](/mobilnisite/slovnik/tdf/)
- [PCC – Performance-oriented Congestion Control](/mobilnisite/slovnik/pcc/)

## Definující specifikace

- **TS 29.213** (Rel-19) — PCC Signalling Flows and QoS Mapping
- **TS 29.217** (Rel-19) — Policy and Charging Control (PCC) for Np Interface

---

📖 **Anglický originál a plná specifikace:** [MUA na 3GPP Explorer](https://3gpp-explorer.com/glossary/mua/)
