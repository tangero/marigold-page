---
slug: "uus3"
url: "/mobilnisite/slovnik/uus3/"
type: "slovnik"
title: "UUS3 – User-to-User Signalling Service 3"
date: 2025-01-01
abbr: "UUS3"
fullName: "User-to-User Signalling Service 3"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/uus3/"
summary: "Doplňková služba v sítích s přepojováním okruhů umožňující transparentní přenos uživatelsky definované signalizační informace v rámci zpráv řízení hovoru. Umožňuje aplikacím vyměňovat data bez nutnost"
---

UUS3 je doplňková služba v sítích s přepojováním okruhů, která umožňuje transparentní přenos uživatelsky definované signalizační informace v rámci zpráv řízení hovoru, což aplikacím umožňuje vyměňovat data bez nutnosti přenosového kanálu.

## Popis

User-to-User Signalling Service 3 (UUS3) je standardizovaná doplňková služba definovaná v rámci domény 3GPP Core Network, konkrétně pro telefonii s přepojováním okruhů ([CS](/mobilnisite/slovnik/cs/)). Jejím hlavním účelem je poskytnout mechanismus pro transparentní přenos omezeného množství uživatelsky generované signalizační informace mezi dvěma uživatelskými zařízeními (UE) během navazování, aktivní fáze nebo ukončení mobilního odchozího nebo příchozího hovoru s přepojováním okruhů. Tento přenos probíhá v rámci existujících signalizačních zpráv protokolu řízení hovoru (např. v rámci zpráv SETUP, ALERTING, CONNECT nebo DISCONNECT), aniž by vyžadoval zřízení samostatného přenosového kanálu. Díky tomu je vysoce efektivní pro krátké výměny dat související s hovorem samotným.

Z architektonického hlediska UUS3 funguje v rámci entity Řízení hovoru ([CC](/mobilnisite/slovnik/cc/)) v UE a v Mobile Switching Centre ([MSC](/mobilnisite/slovnik/msc/)) sítě. Službu vyvolává volající UE, které zahrne informační prvky [UUS](/mobilnisite/slovnik/uus/) do své zprávy pro navázání hovoru. MSC po jejich přijetí zkontroluje předplatné a kompatibilitu služby, než transparentně přepošle UUS data směrem k volané straně v rámci příslušné signalizace [ISDN](/mobilnisite/slovnik/isdn/) User Part ([ISUP](/mobilnisite/slovnik/isup/)) nebo Bearer Independent Call Control (BICC). Entita CC přijímajícího UE tuto informaci extrahuje a předá ji příslušné aplikaci. Služba definuje tři typy provozu: typ 1 (během navazování hovoru), typ 2 (dostupný po celou dobu hovoru) a typ 3 (specifický pro síť).

Klíčovými součástmi jsou informační prvek UUS, který obsahuje uživatelská data a identifikátor protokolu určující jejich formát, a servisní logika v MSC pro autorizaci a transparentní směrování. Její role byla v pre-IMS sítích klíčová pro umožnění interaktivních přidaných služeb. Mohla být například použita k odeslání čísla telefonní karty, servisního kódu nebo autentizačních tokenů přímo v rámci signalizace hovoru, což umožnilo přijímající aplikaci tato data zpracovat před nebo během spojení hovoru. Tento mechanismus před rozšířeným nasazením přepojování paketů pro data během hovoru poskytoval plynulý způsob integrace telefonie s datovými službami.

## K čemu slouží

UUS3 byla vytvořena, aby řešila omezení tradičních hlasově orientovaných sítí s přepojováním okruhů, kterým chyběla standardizovaná, v pásmově provázaná metoda pro výměnu signalizačních dat mezi aplikacemi. Před její standardizací vyžadovala implementace interaktivních služeb, jako je ověření telefonní karty, služeb řízených menu nebo interakcí klient-server během hovoru, buď komplexní signalizaci pomocí vícefrekvenčních tónů ([DTMF](/mobilnisite/slovnik/dtmf/)) po spojení, nebo zřízení samostatného datového kanálu, což bylo neefektivní a pomalé. Historickým kontextem je vývoj sítí GSM a UMTS, kde operátoři usilovali o zavedení služeb inteligentní sítě ([IN](/mobilnisite/slovnik/in/)) a přidaných služeb bez nutnosti přestavby základní architektury s přepojováním okruhů.

Řešila problém transparentnosti služeb a interoperability tím, že poskytla čistý, protokolem definovaný 'vedlejší kanál' v rámci nativní signalizace řízení hovoru. To umožnilo síťovým operátorům a poskytovatelům služeb třetích stran vyvíjet aplikace, které mohly komunikovat potřebná data (jako identity uživatelů, servisní klíče nebo identifikátory transakcí) přímo v čase navazování hovoru. To bylo zvláště důležité pro systémy předplacených služeb, služby virtuální privátní sítě (VPN) a služby upozorňování na hovory, kde síť potřebovala od volajícího dodatečné informace před rozhodnutím, jak hovor směrovat nebo zpracovat. UUS3 v podstatě překlenula propast mezi čistě hlasovou telefonií a rostoucí poptávkou po integrovaných datových službách v rámci omezení existujícího jádra CS.

## Klíčové vlastnosti

- Transparentní přenos uživatelských dat v rámci signalizačních zpráv řízení hovoru (SETUP, CONNECT atd.)
- Provoz definován pro navazování hovoru (typ 1), celou dobu hovoru (typ 2) a specifické použití v síti (typ 3)
- Obsahuje identifikátor protokolu pro rozlišení různých formátů uživatelských dat a aplikací
- Vyžaduje kontrolu předplatného a autorizaci služby ze strany MSC
- Nevyžaduje zřízení přenosového kanálu pro přenos dat
- Podporuje scénáře jak mobilních odchozích, tak příchozích hovorů

## Související pojmy

- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)
- [ISUP – MIME ISDN User Part Multi-purpose Internet Mail Extension](/mobilnisite/slovnik/isup/)

## Definující specifikace

- **TS 23.087** (Rel-19) — User-to-User Signalling (UUS) Stage 2
- **TS 24.087** (Rel-19) — User-to-User Signalling (UUS) Stage 3

---

📖 **Anglický originál a plná specifikace:** [UUS3 na 3GPP Explorer](https://3gpp-explorer.com/glossary/uus3/)
