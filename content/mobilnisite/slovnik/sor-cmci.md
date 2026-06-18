---
slug: "sor-cmci"
url: "/mobilnisite/slovnik/sor-cmci/"
type: "slovnik"
title: "SOR-CMCI – Steering of Roaming Connected Mode Control Information"
date: 2025-01-01
abbr: "SOR-CMCI"
fullName: "Steering of Roaming Connected Mode Control Information"
category: "Mobility"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/sor-cmci/"
summary: "SOR-CMCI je parametr zaslaný UE v připojeném režimu, který jí přikazuje aplikovat informace pro řízení roamingu (Steering of Roaming) okamžitě nebo při dalším nečinném režimu. Zajišťuje včasné provede"
---

SOR-CMCI je parametr zaslaný UE v připojeném režimu, který jí přikazuje okamžitou nebo následnou aplikaci informací pro řízení roamingu (Steering of Roaming) při přechodu do nečinného režimu, čímž zajišťuje včasné síťové přesměrování pro správu provozu a optimalizaci roamingu.

## Popis

Steering of Roaming Connected Mode Control Information (SOR-CMCI) je řídicí mechanismus zavedený ve specifikaci 3GPP Release 17, který funguje ve spojení s daty pro řízení roamingu (Steering of Roaming, [SOR](/mobilnisite/slovnik/sor/)). Jedná se o parametr doručený sítí uživatelskému zařízení (UE), které je v připojeném režimu (např. [RRC](/mobilnisite/slovnik/rrc/)_CONNECTED v NG-RAN), a který poskytuje instrukce, kdy má UE nově přijaté SOR informace zpracovat a aplikovat. SOR-CMCI je obsažen v transparentním kontejneru SOR, který je od funkce [AMF](/mobilnisite/slovnik/amf/) (Access and Mobility Management Function) zaslán UE prostřednictvím zprávy DOWNLINK [NAS](/mobilnisite/slovnik/nas/) TRANSPORT.

Transparentní kontejner SOR, definovaný v 3GPP TS 24.501, přenáší samotná SOR data a přidružený parametr SOR-CMCI. Parametr SOR-CMCI je 3bitové pole, které přenáší konkrétní příkazy pro UE. Hlavními příkazy jsou: 'aplikovat okamžitě' a 'aplikovat v nečinném režimu'. Když UE obdrží SOR informace s indikací 'aplikovat okamžitě', musí okamžitě zahájit proceduru řízení roamingu, i když je v připojeném režimu. To typicky znamená, že UE opustí připojený režim, vyhodnotí preferovaný seznam [PLMN](/mobilnisite/slovnik/plmn/) ze SOR dat a případně vybere novou buňku/PLMN, což může spustit registrační proceduru v nové síti.

Pokud SOR-CMCI indikuje 'aplikovat v nečinném režimu', UE SOR informace uloží a jejich aplikaci odloží až do dalšího přechodu do nečinného režimu (např. po uvolnění RRC spojení). Tento mechanismus dává síti přesnou kontrolu nad načasováním akce přesměrování. Zavedení SOR-CMCI řeší klíčový scénář: bez něj by UE v připojeném režimu, které obdrží SOR data, mohlo jejich aplikaci odložit na neurčitý pozdější čas, což by potenciálně oddálilo kritická síťová rozhodnutí o přesměrování. Zabezpečený paket uvnitř SOR dat, který je pro UE integritně chráněn a šifrován, také obsahuje hash hodnotu SOR-CMCI, čímž zajišťuje jeho autenticitu a zabraňuje manipulaci.

## K čemu slouží

SOR-CMCI byl zaveden, aby vyřešil problém s nejednoznačností načasování spojeným s doručováním informací pro řízení roamingu (Steering of Roaming) UE, které je aktivně v připojené relaci. V původních procedurách [SOR](/mobilnisite/slovnik/sor/) z Release 16, když byla SOR data zaslána UE v připojeném režimu, standard výslovně nenařizoval, kdy má UE provést proceduru přesměrování. To mohlo vést k nepředvídatelnému chování a zpožděním, což podkopávalo schopnost operátora dynamicky spravovat roamingový provoz téměř v reálném čase. Pro efektivní přesměrování provozu, zejména jako reakci na měnící se síťové podmínky nebo komerční podněty, potřebuje domácí operátor jistotu, kdy bude politika přesměrování provedena.

Vytvoření SOR-CMCI poskytuje síti explicitní kontrolu, umožňuje jí nařídit okamžitou akci přesměrování (která může přerušit probíhající relaci) nebo ji naplánovat na vhodnější dobu (při dalším nečinném režimu). To umožňuje sofistikovanější a spolehlivější strategie správy roamingu. Například operátor může použít 'aplikovat okamžitě' pro urgentní přesměrování od přetížené partnerské sítě, zatímco 'aplikovat v nečinném režimu' použije pro méně časově kritické aktualizace politik, čímž zlepšuje jak síťovou efektivitu, tak uživatelský zážitek tím, že se tam, kde je to možné, vyhne zbytečným přerušením relace.

## Klíčové vlastnosti

- 3bitový řídicí parametr doručovaný v transparentním kontejneru SOR.
- Poskytuje explicitní příkazy: 'aplikovat okamžitě' nebo 'aplikovat v nečinném režimu'.
- Umožňuje síti řídit načasování provedení SOR politik.
- Aplikovatelné pro UE v režimu RRC_CONNECTED / připojeném NAS režimu N1.
- Integrita SOR-CMCI je chráněna jeho zahrnutím do hashe zabezpečeného paketu.
- Zajišťuje předvídatelné chování UE pro dynamickou správu roamingu.

## Související pojmy

- [SOR-AF – Steering Of Roaming Application Function](/mobilnisite/slovnik/sor-af/)

## Definující specifikace

- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 31.111** (Rel-19) — USIM Application Toolkit (USAT) Specification

---

📖 **Anglický originál a plná specifikace:** [SOR-CMCI na 3GPP Explorer](https://3gpp-explorer.com/glossary/sor-cmci/)
