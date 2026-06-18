---
slug: "tmc"
url: "/mobilnisite/slovnik/tmc/"
type: "slovnik"
title: "TMC – Test Mode Control"
date: 2024-01-01
abbr: "TMC"
fullName: "Test Mode Control"
category: "Management"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/tmc/"
summary: "TMC je rámec definovaný pro 5G NR pro řízení testovacích režimů ve uživatelském zařízení (UE) a síti během testování shody a výkonu. Poskytuje standardizované postupy pro aktivaci, konfiguraci a deakt"
---

TMC je rámec 3GPP pro řízení testovacích režimů v zařízeních a sítích 5G NR za účelem umožnění standardizovaného, reprodukovatelného testování pro ověřování shody a výkonu.

## Popis

Test Mode Control (TMC) je rámec pro správu a řízení specifikovaný v testovacích specifikacích pro 5G New Radio (NR), především v 3GPP TS 38.509. Definuje postupy a signalizaci potřebné k převedení uživatelského zařízení (UE) nebo síťové testovací techniky do řízeného testovacího režimu. Tyto testovací režimy jsou nezbytné pro provádění reprodukovatelného testování shody, ověřování výkonnosti v rádiové části ([RF](/mobilnisite/slovnik/rf/)) a testů signalizace protokolů v laboratorním nebo řízeném terénním prostředí. TMC funguje tak, že mezi testovacím systémem (vystupujícím jako testovací řadič) a testovaným zařízením ([DUT](/mobilnisite/slovnik/dut/)), kterým může být UE nebo gNodeB (gNB) v síťových testovacích scénářích, vytvoří vyhrazený řídicí kanál.

Architektura TMC zahrnuje specifické příkazy pro testovací režim a konfigurační zprávy. Testovací řadič pomocí těchto zpráv instruuje DUT, aby přepsalo své běžné provozní chování. Pro UE to může zahrnovat vynucení specifických stavů řízení rádiových prostředků ([RRC](/mobilnisite/slovnik/rrc/)), aplikaci předdefinovaných podmínek kanálu, ignorování určitých systémových informačních bloků ([SIB](/mobilnisite/slovnik/sib/)) nebo generování standardizovaných vzorců testovacího provozu. Pro testování síťového zařízení může TMC řídit gNB tak, aby emulovalo konkrétní chování UE nebo degradace rádiového kanálu. Rámec zajišťuje, že DUT funguje deterministickým způsobem, izoluje testovanou proměnnou od nepředvídatelných síťových podmínek nebo interakcí uživatele.

Klíčové součásti TMC zahrnují postup aktivace testovacího režimu, sadu testovacích konfiguračních parametrů a deaktivaci testovacího režimu. Aktivace obvykle vyžaduje zabezpečený handshake nebo předdefinovaný spouštěč (např. specifický testovací servisní požadavek). Po aktivaci může testovací řadič dynamicky přeconfigurovat testovací parametry. TMC také definuje, jak DUT hlásí testovací měření a stav zpět řadiči. Tato obousměrná komunikace je zásadní pro automatizované provádění testů. Design rámce je těsně integrován s dalšími testovacími specifikacemi, jako jsou ty pro RF (TS 38.521) a Protokol (TS 38.523), a poskytuje řídicí rovinu potřebnou k nastavení přesných podmínek požadovaných těmito testovacími případy.

## K čemu slouží

TMC bylo zavedeno v 3GPP Release 15, aby řešilo rostoucí složitost a přísné požadavky testování zařízení a sítí 5G NR. Před jeho standardizací bylo řízení testovacího režimu často implementováno prostřednictvím proprietárních, výrobci specifických příkazů nebo fyzických rozhraní (jako speciální testovací konektory). Tento nedostatek jednotnosti ztěžoval zkušebnám, regulátorům a operátorům vytváření konzistentních, automatizovaných testovacích prostředí, zejména pro testování interoperability více dodavatelů.

Primární problém, který TMC řeší, je potřeba standardizované metody pro řízení chování zařízení během testování, která je schopná práce přes vzduch ([OTA](/mobilnisite/slovnik/ota/)). Jak se zařízení 5G stala více integrovanými (např. s neodnímatelnými anténami a uzavřenými konstrukcemi), závislost na fyzických testovacích portech poklesla. TMC poskytuje řešení založené na protokolu, které funguje přes běžné rádiové rozhraní, a umožňuje tak vzdálené a automatizované provádění testů. To je klíčové pro efektivní ověřování obrovského množství funkcí 5G, frekvenčních pásem a scénářů nasazení.

K jeho vytvoření vedl snahou průmyslu o rychlejší uvedení 5G zařízení na trh při současném zajištění vysoké kvality a shody s globálními standardy. Tím, že poskytuje společný „jazyk“ pro testovací řízení, TMC snižuje náklady na vývoj a testování jak pro výrobce zařízení, tak pro dodavatele testovací techniky. Zajišťuje, že testy shody jsou prováděny za identických, opakovatelných podmínek po celém světě, což je zásadní pro certifikační orgány jako Global Certification Forum ([GCF](/mobilnisite/slovnik/gcf/)) a PTCRB. TMC tedy hraje základní roli v zajišťování kvality a interoperability ekosystému 5G.

## Klíčové vlastnosti

- Standardizovaná aktivace a deaktivace testovacích režimů přes vzduch (OTA)
- Řízení stavu RRC UE a konfigurace rádiových prostředků pro testování
- Konfigurace testovacích parametrů fyzické vrstvy a podmínek kanálu specifických pro testy
- Vstřikování a monitorování standardizovaných vzorců testovacího datového provozu
- Podpora scénářů testování jak uživatelských zařízení (UE), tak síťového vybavení (gNB)
- Integrace s testovacími případy pro ověřování shody protokolů a RF definovanými 3GPP

## Související pojmy

- [UE – User Equipment](/mobilnisite/slovnik/ue/)
- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)

## Definující specifikace

- **TS 38.509** (Rel-18) — Special conformance testing functions for UE

---

📖 **Anglický originál a plná specifikace:** [TMC na 3GPP Explorer](https://3gpp-explorer.com/glossary/tmc/)
