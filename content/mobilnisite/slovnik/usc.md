---
slug: "usc"
url: "/mobilnisite/slovnik/usc/"
type: "slovnik"
title: "USC – UE Service Capabilities"
date: 2025-01-01
abbr: "USC"
fullName: "UE Service Capabilities"
category: "Services"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/usc/"
summary: "USC označuje soubor služeb a funkcí, které může uživatelské zařízení (UE) podporovat, jako je například hlas přes LTE (VoLTE) nebo videohovory. Síť jej využívá k určení vhodného zpracování služeb a za"
---

USC je soubor služeb a funkcí, které může uživatelské zařízení (UE) podporovat, a který síť využívá k určení vhodného zpracování služeb a zajištění kompatibility pro optimalizované poskytování služeb.

## Popis

UE Service Capabilities (USC) označují soubor služeb a funkcí, které je uživatelské zařízení (UE) schopno podporovat v rámci sítě 3GPP. Tyto schopnosti zahrnují širokou škálu funkcionalit, včetně, ale nejen, hlasových služeb (např. VoLTE, VoNR), videoslužeb, zasílání zpráv (např. [SMS](/mobilnisite/slovnik/sms/), [MMS](/mobilnisite/slovnik/mms/)), datových služeb a doplňkových služeb, jako je čekání na hovor nebo konferenční hovory. USC jsou typicky sdělovány sítí zařízením UE během procesů registrace nebo navazování relace, což umožňuje síťovým prvkům přizpůsobit poskytování služeb podle toho, co zařízení zvládne.

Z architektonického hlediska jsou informace o USC vyměňovány prostřednictvím signalizačních protokolů mezi UE a uzly jádra sítě, jako je Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v LTE nebo Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) v 5G. UE zahrnuje své servisní schopnosti do zpráv, jako je Attach Request nebo Registration Request, často zakódované jako bitové mapy nebo informační prvky, které indikují podporované služby. Síť tyto informace ukládá v databázích účastníků, jako je Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)), a využívá je během autorizace služeb a správy relací. Například, pokud UE indikuje podporu hlasu založeného na IMS, může síť směrovat hlasové hovory přes IP namísto přepojování na okruhově spínaný pádový režim.

Klíčové komponenty zapojené do USC zahrnují softwarové a hardwarové konfigurace UE, které určují jeho schopnosti, signalizační protokoly (např. [NAS](/mobilnisite/slovnik/nas/), [SIP](/mobilnisite/slovnik/sip/)), které přenášejí informace o USC, a síťové funkce, které tato data zpracovávají. USC funguje tak, že umožňuje síti provádět porovnávání schopností – zajišťuje, že služby vyvolané uživatelem jsou kompatibilní s UE. Tím se předchází selháním služeb nebo zhoršeným uživatelským zážitkům, jako je pokus o videohovor na zařízení, které podporuje pouze audio. Dále může USC ovlivnit výběr sítě, přidělování prostředků a aktivaci funkcí, čímž přispívá k efektivnímu využití zdrojů a zlepšené kvalitě služeb.

Její role v síti je klíčová pro personalizaci služeb a interoperabilitu. Díky porozumění USC mohou operátoři služby optimálně poskytovat, vyhnout se zbytečné síťové zátěži z nepodporovaných funkcí a umožnit pokročilé služby, jako jsou Rich Communication Services (RCS) nebo síťové řezy, na základě připravenosti zařízení. Specifikace jako TS 21.904 a TS 21.905 podrobně popisují parametry USC a jejich použití napříč vydáními, což odráží její vývoj spolu s zaváděním nových služeb. USC zajišťuje, že se síť přizpůsobuje různorodému ekosystému zařízení, od základních mobilních telefonů po sofistikované smartphony, a udržuje tak konzistentní kvalitu služeb a spokojenost uživatelů.

## K čemu slouží

USC byly vyvinuty pro řešení heterogenity uživatelských zařízení v mobilních sítích, kde se zařízení výrazně liší v podporovaných službách a funkcích. Řeší problém nekompatibility služeb tím, že umožňuje síti předem zjistit schopnosti zařízení, a tím se vyhnout pokusům o poskytnutí služeb, které UE nezvládne. Tím se zlepšuje uživatelský zážitek, snižuje se počet signalizačních chyb a optimalizuje se využití síťových prostředků.

Historicky nabízely rané mobilní sítě omezené služby a schopnosti zařízení byly relativně jednotné. Jak se sítě vyvíjely, aby podporovaly multimediální a IP služby, rostl rozdíl mezi pokročilými a základními zařízeními, což vedlo k problémům, jako jsou neúspěšná navázání hovorů nebo suboptimální záložní řešení služeb. Zavedení USC ve 3GPP Release 99 poskytlo standardizovaný mechanismus, pomocí kterého mohou UE inzerovat své schopnosti, což umožňuje sítím činit informovaná rozhodnutí o poskytování služeb a směrování.

Motivace pro USC vychází z potřeby efektivní správy služeb v prostředích s více službami, jako je IMS a 5G. Podporuje poskytování komplexních služeb, jako je video ve vysokém rozlišení nebo hraní her v reálném čase, tím, že zajišťuje, že je obdrží pouze schopná zařízení. USC také usnadňuje inovace, protože nové služby mohou být uvedeny s jistotou, že je kompatibilní zařízení budou využívat správně, zatímco starší zařízení jsou šetrně ošetřena. Tato signalizace schopností je zásadní pro dosažení plynulého vývoje služeb a udržení zpětné kompatibility v stále více různorodém prostředí zařízení.

## Klíčové vlastnosti

- Signalizace podporovaných služeb (např. hlas, video, zasílání zpráv) z UE do sítě
- Umožňuje síťovou adaptaci a optimalizaci služeb
- Podporuje porovnávání schopností, aby se předešlo selháním při poskytování služeb
- Usnadňuje efektivní přidělování prostředků na základě funkcí zařízení
- Integruje se s databázemi účastníků pro trvalé uložení informací o schopnostech
- Umožňuje dynamické aktualizace při změně schopností zařízení (např. prostřednictvím softwarových aktualizací)

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TR 21.904** (Rel-4) — 3GPP UE Baseline Capability Requirements
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [USC na 3GPP Explorer](https://3gpp-explorer.com/glossary/usc/)
