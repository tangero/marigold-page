---
slug: "ga-rrc"
url: "/mobilnisite/slovnik/ga-rrc/"
type: "slovnik"
title: "GA-RRC – Generic Access - Radio Resource Control"
date: 2025-01-01
abbr: "GA-RRC"
fullName: "Generic Access - Radio Resource Control"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ga-rrc/"
summary: "Protokol v síti Generic Access Network (GAN), který spravuje rádiové zdroje a mobilitu pro IP přístupovou větev. Adaptuje principy buněčného protokolu RRC pro řízení nelicencovaného rádiového spoje (n"
---

GA-RRC je protokol v síti Generic Access Network, který spravuje rádiové zdroje a mobilitu pro IP přístupovou větev tím, že adaptuje buněčné principy pro řízení nelicencovaného rádiového spoje, jako je Wi-Fi.

## Popis

GA-RRC (Generic Access - Radio Resource Control) je protokol v architektuře sítě Generic Access Network ([GAN](/mobilnisite/slovnik/gan/)) podle 3GPP, který funguje jako adaptační vrstva pro správu rádiových zdrojů a mobility přes nelicencovanou IP přístupovou síť. Působí mezi stanicí Generic Access - Mobile Station (GA-MS) a řadičem Generic Access Network Controller ([GANC](/mobilnisite/slovnik/ganc/)). Zatímco 'rádiový' v jeho názvu odkazuje na nelicencovaný bezdrátový spoj (např. Wi-Fi, Bluetooth), role GA-RRC spočívá v emulaci a rozhraní s procedurami buněčného protokolu Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)) sítí [GERAN](/mobilnisite/slovnik/geran/) nebo UTRAN, což umožňuje jádrové síti spravovat zařízení na IP přístupu, jako by bylo na standardní buněčné rádiové přístupové síti.

Architektonicky je GA-RRC protokolem typu peer-to-peer, který přenáší zprávy podobné RRC přes zabezpečené IP spojení navázané protokolem [GA-RC](/mobilnisite/slovnik/ga-rc/). Jeho klíčovou odpovědností je přenos informací pro správu rádiových zdrojů mezi GA-MS a GANC. To zahrnuje vysílání systémových informací (jako je virtuální identita buňky a parametry) z GANC do GA-MS a předávání měřících hlášení z GA-MS (např. síla signálu Wi-Fi, měření buněčných pilotních signálů) do GANC. GANC využívá tato hlášení spolu s pokyny jádrové sítě k rozhodování o předání spojení. Pro předání spojení z GAN do GERAN/UTRAN se protokol GA-RRC používá k doručení podrobného příkazu k předání (včetně parametrů cílové buňky) z jádrové sítě přes GANC do mobilní stanice.

GA-RRC funguje tak, že zapouzdřuje standardní zprávy GERAN RRC nebo UTRAN RRC do svých protokolových datových jednotek (PDU) pro přenos přes IP rozhraní Up. Nespravuje přímo fyzický Wi-Fi spoj – to zajišťují podřízené protokoly [IEEE](/mobilnisite/slovnik/ieee/) 802.11 – ale poskytuje nezbytnou abstrakci a tok informací pro algoritmy správy rádiových zdrojů (RRM) mobilního jádra. Mezi klíčové procedury zprostředkované GA-RRC patří vysílání GA-RRC SYSTEM INFORMATION, GA-RRC MEASUREMENT CONTROL and REPORTING a příprava a provedení GA-RRC HANDOVER. Jedná se o klíčovou komponentu pro zajištění plynulé mobility, neboť poskytuje řídicí mechanismus, pomocí kterého síť může nařídit mobilní stanici opustit IP přístupový bod a naladit se na konkrétní buněčnou frekvenci a kanál během předání spojení, čímž zajišťuje kontinuitu aktivního hovoru nebo datové relace.

## K čemu slouží

Účelem GA-RRC bylo překlenout propast mezi přístupem k řízení zdrojů tradičních buněčných sítí s přepojováním okruhů a paketově orientovanou, 'best-effort' povahou nelicencovaného IP přístupu. V čistě buněčné síti je [RRC](/mobilnisite/slovnik/rrc/) odpovědný za přímé řízení rádiového spoje. [GAN](/mobilnisite/slovnik/gan/) zavedla transportní vrstvu IP, proto byl potřeba nový protokol pro přenos podstatných RRC informací tímto IP tunelem. GA-RRC vyřešil problém, jak funkce BSC nebo RNC jádrové sítě (nyní umístěné v nebo propojené přes GANC) mohly stále vykonávat kontrolu nad rozhodnutími o mobilitě a rádiových zdrojích pro zařízení připojené přes Wi-Fi.

Bez GA-RRC by síť byla slepá k rádiovým podmínkám IP přístupové větve a nebyla by schopna koordinovat řízená předání spojení. Předchozí pokusy o konvergenci často vedly ke scénářům 'break-before-make', kdy by se Wi-Fi hovor přerušil dříve, než by mohl být navázán buněčný hovor. GA-RRC umožnil předání spojení typu 'make-before-break' tím, že poskytl signalizační kanál pro přípravu buněčné strany, zatímco hovor byl stále aktivní na Wi-Fi. Byl motivován požadavkem na služební kontinuitu na úrovni operátora, která vyžadovala, aby předání spojení byla řízena sítí, rychlá a spolehlivá. GA-RRC převedl rádiové příkazy jádrové sítě do formy přenosné přes IP a hlásil zpět měření ze zařízení, čímž rozšířil dosah buněčné správy rádiových zdrojů (RRM) do nelicencované domény.

## Klíčové vlastnosti

- Přenáší buněčné RRC zprávy (GERAN/UTRAN) přes GAN IP rozhraní
- Vysílá virtuální systémové informace z GANC do GA-MS v IP síti
- Předává měřící hlášení z mobilní stanice (pro IP i buněčná rádia) do sítě
- Umožňuje přípravu a doručení příkazu k síťově řízenému předání spojení mezi GAN a buněčným přístupem
- Poskytuje abstrakční vrstvu pro správu rádiových zdrojů přes nelicencovaný IP transport
- Spolupracuje s GA-RC pro zabezpečený transport a s GA-CSR/PSR pro kontinuitu služeb

## Související pojmy

- [GA-RC – Generic Access - Resource Control](/mobilnisite/slovnik/ga-rc/)
- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)
- [GANC – Generic Access Network Controller](/mobilnisite/slovnik/ganc/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)

## Definující specifikace

- **TS 43.318** (Rel-19) — Generic Access Network (GAN) Stage 2
- **TR 43.902** (Rel-19) — GAN Enhancements Feasibility Study
- **TS 44.318** (Rel-19) — Generic Access Network (GAN) Interface Procedures

---

📖 **Anglický originál a plná specifikace:** [GA-RRC na 3GPP Explorer](https://3gpp-explorer.com/glossary/ga-rrc/)
